import re

PATTERN_ASS_TAGS = re.compile(r'\{[^}]+\}')

S_FORMAT = 'Format:'
S_DIALOGUE = 'Dialogue:'

FIELD_SEP = ','

def remove_line_type(s1: str, s2: str) -> str:
  return s1.removeprefix(s2).lstrip()

def dropout_parse_ass(s: str):
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

  n_crap_fields = field_count - 1

  for line in lines:
    if line.startswith('['):
      # we're out of Events section
      break

    if not line.startswith(S_DIALOGUE):
      continue

    fields = remove_line_type(line, S_DIALOGUE).split(FIELD_SEP, maxsplit=n_crap_fields)

    assert len(fields) == field_count, 'incorrect field count'

    cleaned_text = PATTERN_ASS_TAGS.sub('', fields[-1]).replace('\\N', '\n')

    yield cleaned_text
