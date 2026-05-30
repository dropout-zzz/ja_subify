import dataclasses
from dataclasses import dataclass
from enum import IntEnum

@dataclass
class PlainAnnotation:
  text: str

  def serialize(self) -> dict:
    return {'text': self.text}

  @classmethod
  def deserialize(cls, d: dict):
    return cls(text=d['text'])

@dataclass
class KanjiCharacters:
  base: str
  reading: str = ''

  def serialize(self) -> dict:
    return {'base': self.base, 'reading': self.reading}

  @classmethod
  def deserialize(cls, d: dict):
    return cls(base=d['base'], reading=d['reading'])

@dataclass
class KanjiAnnotation:
  fragments: list[KanjiCharacters] = dataclasses.field(default_factory=list)

  def serialize(self) -> dict:
    return {'fragments': [x.serialize() for x in self.fragments]}

  @classmethod
  def deserialize(cls, d: dict):
    return cls(fragments=[KanjiCharacters.deserialize(x) for x in d['fragments']])

@dataclass
class LoanAnnotation:
  base: str
  romanized: str = ''

  def serialize(self) -> dict:
    return {'base': self.base, 'romanized': self.romanized}

  @classmethod
  def deserialize(cls, d: dict):
    return cls(base=d['base'], romanized=d['romanized'])

class AnnotationType(IntEnum):
  PLAIN_ANNOTATION = 0
  KANJI_ANNOTATION = 1
  LOAN_ANNOTATION = 2

@dataclass
class Annotation:
  inner: PlainAnnotation | KanjiAnnotation | LoanAnnotation
  unfinished: bool = False
  ignore: bool = False
  checked: bool = False

  def serialize(self) -> dict:
    if isinstance(self.inner, PlainAnnotation):
      kind = AnnotationType.PLAIN_ANNOTATION
    elif isinstance(self.inner, KanjiAnnotation):
      kind = AnnotationType.KANJI_ANNOTATION
    elif isinstance(self.inner, LoanAnnotation):
      kind = AnnotationType.LOAN_ANNOTATION
    else:
      raise AssertionError('unhandled annotation type')

    return {
      'unfinished': self.unfinished,
      'ignore': self.ignore,
      'checked': self.checked,
      'type': int(kind),
      'inner': self.inner.serialize(),
    }

  @classmethod
  def deserialize(cls, d: dict):
    kind = d['type']
    match kind:
      case AnnotationType.PLAIN_ANNOTATION:
        inner = PlainAnnotation.deserialize(d['inner'])
      case AnnotationType.KANJI_ANNOTATION:
        inner = KanjiAnnotation.deserialize(d['inner'])
      case AnnotationType.LOAN_ANNOTATION:
        inner = LoanAnnotation.deserialize(d['inner'])
      case _:
        raise ValueError(f'unhandled annotation type {kind}')

    return cls(
      unfinished=d['unfinished'],
      ignore=d['ignore'],
      checked=d['checked'],
      inner=inner,
    )

@dataclass
class DialogueLine:
  fragments: list[Annotation] = dataclasses.field(default_factory=list)

  def serialize(self) -> dict:
    return {'fragments': [x.serialize() for x in self.fragments]}

  @classmethod
  def deserialize(cls, d: dict):
    return cls(fragments=[Annotation.deserialize(x) for x in d['fragments']])

VER_CURRENT = 0

@dataclass
class AnnotationFile:
  version: int = VER_CURRENT
  lines: list[DialogueLine] = dataclasses.field(default_factory=list)

  def serialize(self) -> dict:
    return {
      'version': self.version,
      'lines': [x.serialize() for x in self.lines],
    }

  @classmethod
  def deserialize(cls, d: dict):
    return cls(
      version=d['version'],
      lines=[DialogueLine.deserialize(x) for x in d['lines']],
    )
