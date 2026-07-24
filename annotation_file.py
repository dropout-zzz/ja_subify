# AF is a relax format in JSON
# unknown keys are ignored
# run validate() for stricter checks

import dataclasses
from dataclasses import dataclass
from enum import IntEnum
import json
import re

@dataclass
class PlainAnnotation:
  """a plain text chunk without ruby."""

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
  """smallest part in a kanji word that has an inseparable reading."""

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
  """a series of kanji_chars that belong to the same word"""

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
  """a loan word."""

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
  """wrapper. for metadata.
     please access the real annotation object via `inner'."""

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

def _serialize_ts(ts: int) -> str:
  tmp, ms = divmod(ts, 1000)
  tmp, secs = divmod(tmp, 60)
  hrs, mins = divmod(tmp, 60)
  return f'{hrs:02}:{mins:02}:{secs:02},{ms:03}'

_PATTERN_TS = re.compile(r'(\d{2}):(\d{2}):(\d{2}),(\d{3})')

def _deserialize_ts(s: str) -> int:
  m = _PATTERN_TS.fullmatch(s)
  hrs, mins, secs, ms = map(int, m.groups())
  return ms + (secs + (mins + hrs * 60) * 60) * 1000

@dataclass
class DialogueLine:
  """total content displayed as a subtitle line."""

  fragments: list[Annotation] = dataclasses.field(default_factory=list)
  start_time: int = 0
  end_time: int = 0

  def copy_timing_from(self, other):
    self.start_time = other.start_time
    self.end_time = other.end_time

  def get_normalized(self) -> str:
    """converts this line back into plaintext again"""
    return ''.join(x.get_normalized() for x in self.fragments)

  def serialize(self, lineno: int = -1) -> dict:
    return {
      'fragments': [x.serialize() for x in self.fragments],
      'start_time': _serialize_ts(self.start_time),
      'end_time': _serialize_ts(self.end_time),

      # these fields are intentionally ignored when reading
      'lineno': lineno,
      'orig_line': self.get_normalized(),
    }

  @classmethod
  def deserialize(cls, d: dict):
    return cls(
      fragments=[Annotation.deserialize(x) for x in d['fragments']],
      start_time=_deserialize_ts(d.get('start_time', '00:00:00,000')),
      end_time=_deserialize_ts(d.get('end_time', '00:00:00,000')),
    )

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
  """parse the input string as
     Annotation File that were previously saved."""
  return AnnotationFile.deserialize(json.loads(s))

def annotation_save(af: AnnotationFile) -> str:
  """format AF object as string that can be stored on disk."""
  return json.dumps(af.serialize(), sort_keys=True, indent=2, ensure_ascii=False)
