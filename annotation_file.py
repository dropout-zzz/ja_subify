from dataclasses import dataclass
from enum import IntEnum

@dataclass
class PlainAnnotation:
  text: str

  def serialize(self) -> dict:
    return {'text': self.text}

@dataclass
class KanjiCharacters:
  base: str
  reading: str

  def serialize(self) -> dict:
    return {'base': self.base, 'reading': self.reading}

@dataclass
class KanjiAnnotation:
  fragments: list[KanjiCharacters]

  def serialize(self) -> dict:
    return {'fragments': [x.serialize() for x in self.fragments]}

@dataclass
class LoanAnnotation:
  base: str
  romanized: str

  def serialize(self) -> dict:
    return {'base': self.base, 'romanized': self.romanized}

class AnnotationType(IntEnum):
  PLAIN_ANNOTATION = 0
  KANJI_ANNOTATION = 1
  LOAN_ANNOTATION = 2

@dataclass
class Annotation:
  unfinished: bool
  ignore: bool
  checked: bool
  kind: AnnotationType
  inner: PlainAnnotation | KanjiAnnotation | LoanAnnotation

  def serialize(self) -> dict:
    return {
      'unfinished': self.unfinished,
      'ignore': self.ignore,
      'checked': self.checked,
      'kind': int(self.kind),
      'inner': self.inner.serialize(),
    }

@dataclass
class DialogueLine:
  fragments: list[Annotation]

  def serialize(self) -> dict:
    return {'fragments': [x.serialize() for x in self.fragments]}

@dataclass
class AnnotationFile:
  lines: list[DialogueLine]

  def serialize(self) -> dict:
    return {'lines': [x.serialize() for x in self.lines]}
