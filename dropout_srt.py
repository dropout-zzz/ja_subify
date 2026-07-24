import re
from common_subtitles import Subtitle

# VLC supports some ASS tags inside SRT
PATTERN_ASS_TAGS = re.compile(r'\{[^}]+\}')

PATTERN_TS = re.compile(r'(\d{2}):(\d{2}):(\d{2}),(\d{3})')

TIMING_SEP = '-->'

def _next_line(it) -> tuple[str, bool]:
  try:
    return next(it), False
  except StopIteration:
    return '', True

def parse_ts(s: str) -> int:
  m = PATTERN_TS.fullmatch(s)
  assert m is not None, 'cant parse timestamp'

  try:
    hrs, mins, secs, ms = map(int, m.groups())
  except ValueError as e:
    raise ValueError('cant parse time value') from e

  return ms + (secs + (mins + hrs * 60) * 60) * 1000

def parse_timing(s: str) -> tuple[int, int]:
  try:
    f_start, f_end = s.split(TIMING_SEP)
  except ValueError as e:
    raise ValueError('cant parse timing line') from e
  return parse_ts(f_start.rstrip()), parse_ts(f_end.strip())

def dropout_parse_srt(s: str):
  """take the input string and parse as SRT.

     returns a generator that emits subtitle lines.

     ASS tags are ignored."""

  lines = iter(s.splitlines())

  while True:
    # skip line number
    _next_line(lines)

    timing_line, _ = _next_line(lines)

    texts = []
    while True:
      line, eof = _next_line(lines)
      if line == '':
        # dialogue boundary
        break
      texts.append(PATTERN_ASS_TAGS.sub('', line))

    if eof and len(texts) == 0:
      break

    yield Subtitle(text='\n'.join(texts), timing=parse_timing(timing_line))
