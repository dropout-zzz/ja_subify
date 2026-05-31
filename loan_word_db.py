from dataclasses import dataclass
import dataclasses

@dataclass
class LoanWord:
  base: str
  romanized: str

@dataclass
class LoanWordList:
  inner: dict[str, LoanWord] = dataclasses.field(default_factory=dict)
  off: int = 0

COL_SEP = '\t'

def append_into_loan_words(lwl: LoanWordList, path: str, word: LoanWord):
  if word.base in lwl.inner:
    raise ValueError('word already exists')
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
  with open(path, 'rb') as f:
    lwl = LoanWordList()

    _load_into_loan_words(lwl, (content := f.read()).decode())
    lwl.off = len(content)

    return lwl

def reload_into_loan_words(lwl: LoanWordList, path: str):
  with open(path, 'rb') as f:
    f.seek(lwl.off)
    _load_into_loan_words(lwl, (new := f.read()).decode())
    lwl.off += len(new)
