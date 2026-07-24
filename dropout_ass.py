import re
from common_subtitles import Subtitle

PATTERN_ASS_TAGS = re.compile(r'\{[^}]+\}')
PATTERN_TS = re.compile(r'(\d):(\d{2}):(\d{2})\.(\d{2})')

S_FORMAT = 'Format:'
S_DIALOGUE = 'Dialogue:'

FIELD_SEP = ','

def remove_line_type(s1: str, s2: str) -> str:
  return s1.removeprefix(s2).lstrip()

def parse_timestamp(s: str) -> int:
  m = PATTERN_TS.fullmatch(s)
  assert m is not None, 'cant parse timestamp'

  try:
    h, m, s, ms = map(int, m.groups())
  except ValueError as e:
    raise ValueError('cant parse time value') from e

  return ms + (s + (m + h * 60) * 60) * 1000

def dropout_parse_ass(s: str):
  """parse the input string as ASS.

     returns a generator that emits subtitle lines.

     ASS tags are dropped, \\N is replaced with newline."""

  lines = iter(s.splitlines())
  for line in lines:
    if line == '[Events]':
      break
  else:
    raise ValueError('did not find Events section')

  try:
    fields_line = next(lines)
  except StopIteration as e:
    raise ValueError('expect Format line') from e

  assert fields_line.startswith(S_FORMAT), 'cannot find Format line'

  field_names = [x.strip() for x in remove_line_type(fields_line, S_FORMAT).split(FIELD_SEP)]
  field_count = len(field_names)

  assert field_count > 0, 'no field found'
  assert field_names[-1] == 'Text', 'Text is not the last field'

  try:
    fid_start = field_names.index('Start')
    fid_end = field_names.index('End')
  except ValueError as e:
    raise ValueError('cant find Start or End field') from e

  n_splits = field_count - 1

  for line in lines:
    if line.startswith('['):
      # we're out of Events section
      break

    if not line.startswith(S_DIALOGUE):
      continue

    fields = remove_line_type(line, S_DIALOGUE).split(FIELD_SEP, maxsplit=n_splits)

    assert len(fields) == field_count, 'incorrect field count'

    cleaned_text = PATTERN_ASS_TAGS.sub('', fields[-1]).replace('\\N', '\n')

    yield Subtitle(text=cleaned_text, timing=(parse_timestamp(fields[fid_start]), parse_timestamp(fields[fid_end])))
