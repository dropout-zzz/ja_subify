import re

PATTERN_ASS_TAGS = re.compile(r'\{[^}]+\}')

def dropout_parse_ass(s):
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

  assert fields_line.startswith('Format:'), 'cannot find Format line'

  field_names = [x.strip() for x in fields_line.removeprefix('Format:').lstrip().split(',')]
  field_count = len(field_names)

  assert field_count > 0, 'no field found'
  assert field_names[-1] == 'Text', 'Text is not the last field'

  n_crap_fields = field_count - 1

  for line in lines:
    if line.startswith('['):
      # we're out of Events section
      break

    if not line.startswith('Dialogue:'):
      continue

    fields = line.removeprefix('Dialogue:').lstrip().split(',', maxsplit=n_crap_fields)

    cleaned_text = PATTERN_ASS_TAGS.sub('', fields[-1])

    yield cleaned_text
