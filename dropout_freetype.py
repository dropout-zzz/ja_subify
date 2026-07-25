from ctypes.util import find_library
from ctypes import CDLL, c_void_p

def _load_freetype():
  name = find_library('freetype')
  if name is None:
    raise OSError('cant find libfreetype')
  return CDLL(name)

_libfreetype = _load_freetype()

class FT_Library(c_void_p):
  pass
