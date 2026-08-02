import sys
from argparse import ArgumentTypeError

def _get_std_handle(mode: str):
  match mode:
    case 'r':
      return sys.stdin
    case 'w' | 'a':
      return sys.stdout
    case 'rb':
      return sys.stdin.buffer
    case 'wb' | 'ab':
      return sys.stdout.buffer
    case _:
      raise AssertionError(f'i don\'t understand this mode: {mode!r}')

class FileType2:
  """similar to the argparse.FileType class.
     this uses utf-8 encoding and LF as newline by default."""

  def __init__(self, mode: str, encoding: str | None = 'utf-8', newline: str = '\n'):
    """open() flags are used for opening new files, and not used if user want stdio."""

    self.__mode = mode
    self.__encoding = encoding
    self.__newline = newline

  def __call__(self, path: str):
    if path == '-':
      # have to ignore open() flags because stdio is already opened
      return _get_std_handle(self.__mode)

    try:
      return open(path, self.__mode, encoding=self.__encoding, newline=self.__newline)
    except OSError as e:
      raise ArgumentTypeError(f'can\'t open {path}: {e.strerror}') from e
