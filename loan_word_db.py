# loan word list is stored in TSV inspired format
#
# this library currently doesnt provide an interface to
# save an existing word list object to disk. use the
# append_into_loan_words() function instead.

from dataclasses import dataclass
import dataclasses

@dataclass
class LoanWord:
  """a word entry in the dictionary."""
  base: str
  romanized: str

@dataclass
class LoanWordList:
  """dictionary.

    `inner' holds a mapping from katakana to
    the word entry for look ups.

    to get the list of entries in the
    file, use inner.values()

    use append_into_loan_words(),
    instead of directly modifying the internal dict."""

  inner: dict[str, LoanWord] = dataclasses.field(default_factory=dict)
  off: int = 0

COL_SEP = '\t'

class LoanWordAlreadyExist(Exception):
  """thrown when trying to append a word that already exist"""
  pass

def append_into_loan_words(lwl: LoanWordList, path: str, word: LoanWord):
  """add a word into the word list object.
     on success,
     this operation also writes the change immediately into disk.

     may throw LoanWordAlreadyExist"""
  if word.base in lwl.inner:
    raise LoanWordAlreadyExist
  with open(path, 'ab') as f:
    lwl.off += f.write(f'{word.base}{COL_SEP}{word.romanized}\n'.encode())
  lwl.inner[word.base] = word

def _load_into_loan_words(lwl: LoanWordList, s: str):
  for line in s.splitlines():
    base, romanized = line.split(COL_SEP)
    if base in lwl.inner:
      raise ValueError(f'duplicate word {base!r}')
    lwl.inner[base] = LoanWord(base=base, romanized=romanized)

def load_loan_words(path: str) -> LoanWordList:
  """read and parse a loan word list file from disk."""
  with open(path, 'rb') as f:
    lwl = LoanWordList()

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
