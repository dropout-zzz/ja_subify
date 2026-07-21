from ctypes import CDLL, POINTER, byref, c_void_p, c_int, c_char_p
from ctypes.util import find_library
from enum import IntEnum

def _load_libfontconfig():
  s = find_library('fontconfig')
  if s is None:
    raise OSError('cannot find libfontconfig')
  return CDLL(s)

_libfontconfig = _load_libfontconfig()

FC_FAMILY = 'family'
FC_FILE = 'file'
FC_INDEX = 'index'

class FcConfig(c_void_p):
  pass

class FcPattern(c_void_p):
  pass

class FcResult(IntEnum):
  Match = 0
  NoMatch = 1
  TypeMismatch = 2
  NoId = 3
  OutOfMemory = 4

class FcMatchKind(IntEnum):
  Pattern = 0

def _null_is_nomem(res, func, args):
  if res is None:
    raise MemoryError
  return res

def _false_is_nomem(res, func, args):
  if res == 0:
    raise MemoryError
  return res

def _assert_result(res: FcResult):
  match res:
    case FcResult.Match:
      return
    case FcResult.NoMatch:
      raise KeyError
    case FcResult.TypeMismatch:
      raise TypeError
    case FcResult.NoId:
      raise IndexError
    case FcResult.OutOfMemory:
      raise MemoryError

def _chk_result(res, func, args):
  _assert_result(FcResult(res))
  return res

_fc_fini = _libfontconfig.FcFini
_fc_fini.argtypes = []
_fc_fini.restype = None

_fc_pattern_create = _libfontconfig.FcPatternCreate
_fc_pattern_create.argtypes = []
_fc_pattern_create.restype = c_void_p
_fc_pattern_create.errcheck = _null_is_nomem

_fc_pattern_destroy = _libfontconfig.FcPatternDestroy
_fc_pattern_destroy.argtypes = [FcPattern]
_fc_pattern_destroy.restype = None

_fc_config_substitute = _libfontconfig.FcConfigSubstitute
_fc_config_substitute.argtypes = [FcConfig, FcPattern, c_int]
_fc_config_substitute.restype = c_int
_fc_config_substitute.errcheck = _false_is_nomem

_fc_config_set_default_substitute = _libfontconfig.FcConfigSetDefaultSubstitute
_fc_config_set_default_substitute.argtypes = [FcConfig, FcPattern]
_fc_config_set_default_substitute.restype = None

_fc_pattern_get_integer = _libfontconfig.FcPatternGetInteger
_fc_pattern_get_integer.argtypes = [FcPattern, c_char_p, c_int, POINTER(c_int)]
_fc_pattern_get_integer.restype = c_int
_fc_pattern_get_integer.errcheck = _chk_result

_fc_pattern_get_string = _libfontconfig.FcPatternGetString
_fc_pattern_get_string.argtypes = [FcPattern, c_char_p, c_int, POINTER(c_char_p)]
_fc_pattern_get_string.restype = c_int
_fc_pattern_get_string.errcheck = _chk_result

_fc_pattern_add_string = _libfontconfig.FcPatternAddString
_fc_pattern_add_string.argtypes = [FcPattern, c_char_p, c_char_p]
_fc_pattern_add_string.restype = c_int
_fc_pattern_add_string.errcheck = _false_is_nomem

_fc_font_match = _libfontconfig.FcFontMatch
_fc_font_match.argtypes = [FcConfig, FcPattern, POINTER(c_int)]
_fc_font_match.restype = c_void_p

def FcFini():
  _fc_fini()

def FcPatternCreate() -> FcPattern:
  return FcPattern(_fc_pattern_create())

def FcPatternDestroy(p: FcPattern):
  _fc_pattern_destroy(p)

def FcConfigSubstitute(config: FcConfig | None, p: FcPattern, kind: FcMatchKind):
  _fc_config_substitute(config, p, kind)

def FcConfigSetDefaultSubstitute(config: FcConfig | None, pattern: FcPattern):
  _fc_config_set_default_substitute(config, pattern)

def FcPatternGetInteger(p: FcPattern, object_: str, n: int) -> int:
  i = c_int()
  _fc_pattern_get_integer(p, object_.encode(), n, byref(i))
  return i.value

def FcPatternGetString(p: FcPattern, object_: str, n: int) -> str:
  s = c_char_p()
  _fc_pattern_get_string(p, object_.encode(), n, byref(s))
  return s.value.decode()

def FcPatternAddString(p: FcPattern, object_: str, s: str):
  _fc_pattern_add_string(p, object_.encode(), s.encode())

def FcFontMatch(config: FcConfig | None, p: FcPattern) -> FcPattern | None:
  result = c_int()
  m = _fc_font_match(config, p, byref(result))
  try:
    _assert_result(FcResult(result.value))
  except KeyError:
    pass
  if m is not None:
    return FcPattern(m)
