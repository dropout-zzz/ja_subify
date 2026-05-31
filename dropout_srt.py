def _next_line(it) -> tuple[str, bool]:
  try:
    return next(it), False
  except StopIteration:
    return '', True

def dropout_parse_srt(s: str):
  lines = iter(s.splitlines())

  while True:
    # skip craps
    _next_line(lines)
    _next_line(lines)

    texts = []
    while True:
      line, eof = _next_line(lines)
      if line == '':
        # dialogue boundary
        break
      texts.append(line)

    if eof and len(texts) == 0:
      break

    yield '\n'.join(texts)
