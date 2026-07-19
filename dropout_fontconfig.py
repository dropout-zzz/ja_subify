from ctypes import CDLL, c_void_p
from ctypes.util import find_library

def _load_libfontconfig():
  s = find_library('fontconfig')
  if s is None:
    raise OSError('cannot find libfontconfig')
  return CDLL(s)

_libfontconfig = _load_libfontconfig()

class FcConfig(c_void_p):
  pass

class FcPattern(c_void_p):
  pass
