# WordDB is a relax format in JSON
# unknown keys are ignored
# run validate() for stricter checks
#
# this library currently doesnt provide an interface to
# save an existing word list object to disk. use the
# append_into_normal_words() function instead.

from dataclasses import dataclass
import dataclasses
from enum import IntEnum
import json

@dataclass
class FragmentIgnore:
  """indicates that this segment do not have ruby."""
  text: str

  def serialize(self) -> dict:
    return {"text": self.text}

  def validate(self):
    if not isinstance(self.text, str):
      raise AssertionError

  @classmethod
  def deserialize(cls, d: dict):
    return cls(text=d['text'])

@dataclass
class FragmentKanjiCharacters:
  """ruby."""
  base: str
  reading: str

  def serialize(self) -> dict:
    return {"base": self.base, "reading": self.reading}

  def validate(self):
    if not isinstance(self.base, str):
      raise AssertionError
    if not isinstance(self.reading, str):
      raise AssertionError

  @classmethod
  def deserialize(cls, d: dict):
    return cls(base=d['base'], reading=d['reading'])

class FragmentType(IntEnum):
  IGNORE = 0
  KANJI_CHARACTERS = 1

@dataclass
class NormalTemplate:
  """a word entry inside the dictionary."""
  base: str
  fragments: list[FragmentIgnore | FragmentKanjiCharacters] = dataclasses.field(default_factory=list)

  def get_normalized(self) -> str:
    """return the word in hiragana only."""
    buff = []

    for fragment in self.fragments:
      if isinstance(fragment, FragmentIgnore):
        buff.append(fragment.text)
      elif isinstance(fragment, FragmentKanjiCharacters):
        buff.append(fragment.reading)
      else:
        raise AssertionError('unhandled fragment type')

    return ''.join(buff)

  def serialize(self) -> dict:
    fragments = []

    for fragment in self.fragments:
      if isinstance(fragment, FragmentIgnore):
        kind = FragmentType.IGNORE
      elif isinstance(fragment, FragmentKanjiCharacters):
        kind = FragmentType.KANJI_CHARACTERS
      else:
        raise AssertionError('unhandled fragment type')

      fragments.append({"type": kind, "inner": fragment.serialize()})

    return {"fragments": fragments, "base": self.base}

  def validate(self):
    if not isinstance(self.fragments, list):
      raise AssertionError
    for fragment in self.fragments:
      if not isinstance(fragment, (FragmentIgnore, FragmentKanjiCharacters)):
        raise AssertionError
      fragment.validate()
    if not isinstance(self.base, str):
      raise AssertionError

  @classmethod
  def deserialize(cls, d: dict):
    fragments = []

    for fragment in d['fragments']:
      kind = FragmentType(fragment['type'])
      match kind:
        case FragmentType.IGNORE:
          fragments.append(FragmentIgnore.deserialize(fragment['inner']))
        case FragmentType.KANJI_CHARACTERS:
          fragments.append(FragmentKanjiCharacters.deserialize(fragment['inner']))
        case _:
          raise ValueError(f'unhandled fragment type {kind}')

    return cls(fragments=fragments, base=d['base'])

@dataclass
class NormalWordList:
  """dictionary.

     `inner' holds a mapping from kanji-hiragana mixed script to the word entry.

     to get total list of words in the list, use inner.values().

     `known' holds known set of reading for given kanji_chars.
     this field is only populated when `count_known' is True.

     the flag should be specified when creating the object or
     when using the load_normal_words() function.

     use append_into_normal_words(),
     instead of directly modifying the internal dict."""

  inner: dict[str, NormalTemplate] = dataclasses.field(default_factory=dict)
  known: set[tuple[str, str]] = dataclasses.field(default_factory=set)
  off: int = 0
  count_known: bool = False

  def check(self):
    for x in self.inner.values():
      x.validate()

def _register_known_normal_words(nwl: NormalWordList, word: NormalTemplate):
  for fragment in word.fragments:
    if not isinstance(fragment, FragmentKanjiCharacters):
      continue
    nwl.known.add((fragment.base, fragment.reading))

class NormalWordAlreadyExist(Exception):
  """thrown when trying to append a word that already exist"""
  pass

def append_into_normal_words(nwl: NormalWordList, path: str, word: NormalTemplate):
  """add a word into the word list object.
     on success,
     this operation also writes the change immediately into disk.

     may throw NormalWordAlreadyExist"""
  if word.base in nwl.inner:
    raise NormalWordAlreadyExist
  with open(path, 'ab') as f:
    n = f.write(json.dumps(word.serialize(), sort_keys=True, ensure_ascii=False).encode())
    f.write(b'\n')
    nwl.off += n + 1
  nwl.inner[word.base] = word
  if nwl.count_known:
    _register_known_normal_words(nwl, word)

def _load_into_normal_words(nwl: NormalWordList, s: str):
  for line in s.splitlines():
    word = NormalTemplate.deserialize(json.loads(line))
    if word.base in nwl.inner:
      raise ValueError(f'duplicate word {word.base!r}')
    nwl.inner[word.base] = word
    if nwl.count_known:
      _register_known_normal_words(nwl, word)

def load_normal_words(path: str, count_known: bool = False) -> NormalWordList:
  """open and parse a WordDB file from disk."""
  with open(path, 'rb') as f:
    nwl = NormalWordList(count_known=count_known)

    _load_into_normal_words(nwl, (content := f.read()).decode())
    nwl.off = len(content)

    return nwl

def reload_into_normal_words(nwl: NormalWordList, path: str):
  """partially read and update the word list object from disk.

     this function only works when new contents were appended at file end.
     behavior is not defined in other cases.

     if the file was fully overwritten, load from scratch again instead."""

  with open(path, 'rb') as f:
    f.seek(nwl.off)
    _load_into_normal_words(nwl, (new := f.read()).decode())
    nwl.off += len(new)
