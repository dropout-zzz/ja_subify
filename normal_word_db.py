from dataclasses import dataclass
import dataclasses
from enum import IntEnum
import json

@dataclass
class FragmentIgnore:
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
  base: str
  fragments: list[FragmentIgnore | FragmentKanjiCharacters] = dataclasses.field(default_factory=list)

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
  pass

def append_into_normal_words(nwl: NormalWordList, path: str, word: NormalTemplate):
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
  with open(path, 'rb') as f:
    nwl = NormalWordList(count_known=count_known)

    _load_into_normal_words(nwl, (content := f.read()).decode())
    nwl.off = len(content)

    return nwl

def reload_into_normal_words(nwl: NormalWordList, path: str):
  with open(path, 'rb') as f:
    f.seek(nwl.off)
    _load_into_normal_words(nwl, (new := f.read()).decode())
    nwl.off += len(new)
