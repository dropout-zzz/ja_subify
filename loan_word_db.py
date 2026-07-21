# loan word list is stored in TSV inspired format
#
# this library currently doesnt provide an interface to
# save an existing word list object to disk. use the
# append_into_loan_words() function instead.

from dataclasses import dataclass
import dataclasses

COL_SEP = '\t'
FRAG_SEP_A = '\x00'
FRAG_SEP_B = ' '

@dataclass
class LoanFragment:
  """smallest part in loan word that can be
     correspond to its form in english."""
  base: str
  romanized: str

@dataclass
class LoanWord:
  """a word entry in the dictionary."""
  base: str
  fragments: list[LoanFragment] = dataclasses.field(default_factory=list)

  def get_normalized(self) -> str:
    """return romanized word."""
    return ' '.join(x.romanized for x in self.fragments)

  def serialize(self) -> str:
    a = []
    b = []

    for x in self.fragments:
      a.append(x.base)
      b.append(x.romanized)

    return f'{FRAG_SEP_A.join(a)}{COL_SEP}{FRAG_SEP_B.join(b)}'

  @classmethod
  def deserialize(cls, s: str):
    a, b = s.split(COL_SEP)
    base_parts = a.split(FRAG_SEP_A)

    fragments = []
    for base, romanized in zip(base_parts, b.split(FRAG_SEP_B), strict=True):
      fragments.append(LoanFragment(base=base, romanized=romanized))

    return cls(fragments=fragments, base=''.join(base_parts))

@dataclass
class LoanWordList:
  """dictionary.

    `inner' holds a mapping from katakana to
    the word entry for look ups.

    to get the list of entries in the
    file, use inner.values()

     `known' holds a mapping for known set of loan word fragments.
     this field is only populated when `count_known' is True.

     the flag should be specified when creating the object or
     when using the load_loan_words() function.

    use append_into_loan_words(),
    instead of directly modifying the internal dict."""

  inner: dict[str, LoanWord] = dataclasses.field(default_factory=dict)
  known: set[tuple[str, str]] = dataclasses.field(default_factory=set)
  off: int = 0
  count_known: bool = False

class LoanWordAlreadyExist(Exception):
  """thrown when trying to append a word that already exist"""
  pass

def _register_known_loan_words(lwl: LoanWordList, word: LoanWord):
  for fragment in word.fragments:
    lwl.known.add((fragment.base, fragment.romanized))

def append_into_loan_words(lwl: LoanWordList, path: str, word: LoanWord):
  """add a word into the word list object.
     on success,
     this operation also writes the change immediately into disk.

     may throw LoanWordAlreadyExist"""
  if word.base in lwl.inner:
    raise LoanWordAlreadyExist

  with open(path, 'ab') as f:
    n = f.write(word.serialize().encode())
    f.write(b'\n')
    lwl.off += n + 1

  lwl.inner[word.base] = word

  if lwl.count_known:
    _register_known_loan_words(lwl, word)

def _load_into_loan_words(lwl: LoanWordList, s: str):
  for line in s.splitlines():
    word = LoanWord.deserialize(line)

    if word.base in lwl.inner:
      raise ValueError(f'duplicate word {word.base!r}')

    lwl.inner[word.base] = word

    if lwl.count_known:
      _register_known_loan_words(lwl, word)

def load_loan_words(path: str, count_known: bool = False) -> LoanWordList:
  """read and parse a loan word list file from disk."""
  with open(path, 'rb') as f:
    lwl = LoanWordList(count_known=count_known)

    _load_into_loan_words(lwl, (content := f.read()).decode())
    lwl.off = len(content)

    return lwl

def reload_into_loan_words(lwl: LoanWordList, path: str):
  """partially read and update the word list object from disk.

     this function only works when new contents were appended at file end.
     behavior is not defined in other cases.

     if the file was fully overwritten, load from scratch again instead."""

  with open(path, 'rb') as f:
    f.seek(lwl.off)
    _load_into_loan_words(lwl, (new := f.read()).decode())
    lwl.off += len(new)
