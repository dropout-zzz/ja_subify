import dataclasses
from dataclasses import dataclass
from enum import IntEnum
import json

@dataclass
class PlainAnnotation:
  text: str

  def get_normalized(self) -> str:
    return self.text

  def serialize(self) -> dict:
    return {'text': self.text}

  @classmethod
  def deserialize(cls, d: dict):
    return cls(text=d['text'])

  def validate(self):
    if not isinstance(self.text, str):
      raise AssertionError

@dataclass
class KanjiCharacters:
  base: str
  reading: str = ''

  def get_normalized(self) -> str:
    return self.base

  def serialize(self) -> dict:
    return {'base': self.base, 'reading': self.reading}

  @classmethod
  def deserialize(cls, d: dict):
    return cls(base=d['base'], reading=d['reading'])

  def validate(self):
    if not isinstance(self.base, str):
      raise AssertionError
    if not isinstance(self.reading, str):
      raise AssertionError

@dataclass
class KanjiAnnotation:
  fragments: list[KanjiCharacters] = dataclasses.field(default_factory=list)

  def get_normalized(self) -> str:
    return ''.join(x.get_normalized() for x in self.fragments)

  def serialize(self) -> dict:
    return {'fragments': [x.serialize() for x in self.fragments]}

  @classmethod
  def deserialize(cls, d: dict):
    return cls(fragments=[KanjiCharacters.deserialize(x) for x in d['fragments']])

  def validate(self):
    if not isinstance(self.fragments, list):
      raise AssertionError
    for x in self.fragments:
      if not isinstance(x, KanjiCharacters):
        raise AssertionError
      x.validate()

@dataclass
class LoanAnnotation:
  base: str
  romanized: str = ''

  def get_normalized(self) -> str:
    return self.base

  def serialize(self) -> dict:
    return {'base': self.base, 'romanized': self.romanized}

  @classmethod
  def deserialize(cls, d: dict):
    return cls(base=d['base'], romanized=d['romanized'])

  def validate(self):
    if not isinstance(self.base, str):
      raise AssertionError
    if not isinstance(self.romanized, str):
      raise AssertionError

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

  def get_normalized(self) -> str:
    return self.inner.get_normalized()

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

  def validate(self):
    if not isinstance(self.inner, (PlainAnnotation, KanjiAnnotation, LoanAnnotation)):
      raise AssertionError
    self.inner.validate()
    if not isinstance(self.unfinished, bool):
      raise AssertionError
    if not isinstance(self.ignore, bool):
      raise AssertionError
    if not isinstance(self.checked, bool):
      raise AssertionError

  @classmethod
  def deserialize(cls, d: dict):
    kind = AnnotationType(d['type'])
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

  def get_normalized(self) -> str:
    return ''.join(x.get_normalized() for x in self.fragments)

  def serialize(self, lineno: int = -1) -> dict:
    return {
      'fragments': [x.serialize() for x in self.fragments],
      'lineno': lineno,
    }

  @classmethod
  def deserialize(cls, d: dict):
    return cls(fragments=[Annotation.deserialize(x) for x in d['fragments']])

  def validate(self):
    if not isinstance(self.fragments, list):
      raise AssertionError
    for x in self.fragments:
      if not isinstance(x, Annotation):
        raise AssertionError
      x.validate()

VER_CURRENT = 0

@dataclass
class AnnotationFile:
  version: int = VER_CURRENT
  lines: list[DialogueLine] = dataclasses.field(default_factory=list)

  def serialize(self) -> dict:
    return {
      'version': self.version,
      'lines': [x.serialize(i) for i, x in enumerate(self.lines, start=1)],
    }

  @classmethod
  def deserialize(cls, d: dict):
    return cls(
      version=d['version'],
      lines=[DialogueLine.deserialize(x) for x in d['lines']],
    )

  def validate(self):
    if not isinstance(self.version, int):
      raise AssertionError
    if not isinstance(self.lines, list):
      raise AssertionError
    for x in self.lines:
      if not isinstance(x, DialogueLine):
        raise AssertionError
      x.validate()

def annotation_parse(s: str) -> AnnotationFile:
  return AnnotationFile.deserialize(json.loads(s))

def annotation_save(af: AnnotationFile) -> str:
  return json.dumps(af.serialize(), sort_keys=True, indent=2, ensure_ascii=False)
