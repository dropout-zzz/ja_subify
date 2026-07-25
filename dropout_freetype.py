from ctypes.util import find_library
from ctypes import CDLL, POINTER, byref, Structure, addressof, c_void_p, c_int, c_long, c_char_p, c_ushort, c_short
from enum import IntEnum
from weakref import finalize
from typing import Any

def _load_freetype():
  name = find_library('freetype')
  if name is None:
    raise OSError('cant find libfreetype')
  return CDLL(name)

_libfreetype = _load_freetype()

class FT_Library(c_void_p):
  pass

class FT_Error(IntEnum):
  Ok = 0
  Cannot_Open_Resource = 1
  Unknown_File_Format = 2
  Invalid_File_Format = 3
  Invalid_Version = 4
  Lower_Module_Version = 5
  Invalid_Argument = 6
  Unimplemented_Feature = 7
  Invalid_Table = 8
  Invalid_Offset = 9
  Array_Too_Large = 10
  Missing_Module = 11
  Missing_Property = 12
  Invalid_Glyph_Index = 16
  Invalid_Character_Code = 17
  Invalid_Glyph_Format = 18
  Cannot_Render_Glyph = 19
  Invalid_Outline = 20
  Invalid_Composite = 21
  Too_Many_Hints = 22
  Invalid_Pixel_Size = 23
  Invalid_SVG_Document = 24
  Invalid_Handle = 32
  Invalid_Library_Handle = 33
  Invalid_Driver_Handle = 34
  Invalid_Face_Handle = 35
  Invalid_Size_Handle = 36
  Invalid_Slot_Handle = 37
  Invalid_CharMap_Handle = 38
  Invalid_Cache_Handle = 39
  Invalid_Stream_Handle = 40
  Too_Many_Drivers = 48
  Too_Many_Extensions = 49
  Out_Of_Memory = 64
  Unlisted_Object = 65
  Cannot_Open_Stream = 81
  Invalid_Stream_Seek = 82
  Invalid_Stream_Skip = 83
  Invalid_Stream_Read = 84
  Invalid_Stream_Operation = 85
  Invalid_Frame_Operation = 86
  Nested_Frame_Access = 87
  Invalid_Frame_Read = 88
  Raster_Uninitialized = 96
  Raster_Corrupted = 97
  Raster_Overflow = 98
  Raster_Negative_Height = 99
  Too_Many_Caches = 112
  Invalid_Opcode = 128
  Too_Few_Arguments = 129
  Stack_Overflow = 130
  Code_Overflow = 131
  Bad_Argument = 132
  Divide_By_Zero = 133
  Invalid_Reference = 134
  Debug_OpCode = 135
  ENDF_In_Exec_Stream = 136
  Nested_DEFS = 137
  Invalid_CodeRange = 138
  Execution_Too_Long = 139
  Too_Many_Function_Defs = 140
  Too_Many_Instruction_Defs = 141
  Table_Missing = 142
  Horiz_Header_Missing = 143
  Locations_Missing = 144
  Name_Table_Missing = 145
  CMap_Table_Missing = 146
  Hmtx_Table_Missing = 147
  Post_Table_Missing = 148
  Invalid_Horiz_Metrics = 149
  Invalid_CharMap_Format = 150
  Invalid_PPem = 151
  Invalid_Vert_Metrics = 152
  Could_Not_Find_Context = 153
  Invalid_Post_Table_Format = 154
  Invalid_Post_Table = 155
  DEF_In_Glyf_Bytecode = 156
  Missing_Bitmap = 157
  Missing_SVG_Hooks = 158
  Syntax_Error = 160
  Stack_Underflow = 161
  Ignore = 162
  No_Unicode_Glyph_Name = 163
  Glyph_Too_Big = 164
  Missing_Startfont_Field = 176
  Missing_Font_Field = 177
  Missing_Size_Field = 178
  Missing_Fontboundingbox_Field = 179
  Missing_Chars_Field = 180
  Missing_Startchar_Field = 181
  Missing_Encoding_Field = 182
  Missing_Bbx_Field = 183
  Bbx_Too_Big = 184
  Corrupted_Font_Header = 185
  Corrupted_Font_Glyphs = 186

class FT_ListRec(Structure):
  pass

class FT_FaceRec(Structure):
  pass

FT_Face = POINTER(FT_FaceRec)

class FT_Generic(Structure):
  pass

FT_Generic._fields_ = [
  ("data", c_void_p),
  ("finalizer", c_void_p),  # FIXME
]

class FT_BBox(Structure):
  pass

FT_BBox._fields_ = [
  ("xMin", c_long),
  ("yMin", c_long),
  ("xMax", c_long),
  ("yMax", c_long),
]

FT_ListRec._fields_ = [
  ("head", c_void_p),  # FIXME
  ("tail", c_void_p),  # FIXME
]

FT_FaceRec._fields_ = [
  ("num_faces", c_long),
  ("face_index", c_long),
  ("face_flags", c_long),
  ("style_flags", c_long),
  ("num_glyphs", c_long),
  ("family_name", c_char_p),
  ("style_name", c_char_p),
  ("num_fixed_sizes", c_int),
  ("available_sizes", c_void_p),  # FIXME
  ("num_charmaps", c_int),
  ("charmaps", c_void_p),  # FIXME
  ("generic", FT_Generic),
  ("bbox", FT_BBox),
  ("units_per_EM", c_ushort),
  ("ascender", c_short),
  ("descender", c_short),
  ("height", c_short),
  ("max_advance_width", c_short),
  ("max_advance_height", c_short),
  ("underline_position", c_short),
  ("underline_thickness", c_short),
  ("glyph", c_void_p),  # FIXME
  ("size", c_void_p),  # FIXME
  ("charmap", c_void_p),  # FIXME
  ("driver", c_void_p),
  ("memory", c_void_p),
  ("stream", c_void_p),  # FIXME
  ("sizes_list", FT_ListRec),
  ("autohint", FT_Generic),
  ("extensions", c_void_p),
  ("internal", c_void_p),
]

class FreetypeException(Exception):
  """an error returned from freetype."""

_ERR_MAP: dict[FT_Error, str] = {
  FT_Error.Cannot_Open_Resource: 'cannot open resource',
  FT_Error.Unknown_File_Format: 'unknown file format',
  FT_Error.Invalid_File_Format: 'broken file',
  FT_Error.Invalid_Version: 'invalid FreeType version',
  FT_Error.Lower_Module_Version: 'module version is too low',
  FT_Error.Invalid_Argument: 'invalid argument',
  FT_Error.Unimplemented_Feature: 'unimplemented feature',
  FT_Error.Invalid_Table: 'broken table',
  FT_Error.Invalid_Offset: 'broken offset within table',
  FT_Error.Array_Too_Large: 'array allocation size too large',
  FT_Error.Missing_Module: 'missing module',
  FT_Error.Missing_Property: 'missing property',
  FT_Error.Invalid_Glyph_Index: 'invalid glyph index',
  FT_Error.Invalid_Character_Code: 'invalid character code',
  FT_Error.Invalid_Glyph_Format: 'unsupported glyph image format',
  FT_Error.Cannot_Render_Glyph: 'cannot render this glyph format',
  FT_Error.Invalid_Outline: 'invalid outline',
  FT_Error.Invalid_Composite: 'invalid composite glyph',
  FT_Error.Too_Many_Hints: 'too many hints',
  FT_Error.Invalid_Pixel_Size: 'invalid pixel size',
  FT_Error.Invalid_SVG_Document: 'invalid SVG document',
  FT_Error.Invalid_Handle: 'invalid object handle',
  FT_Error.Invalid_Library_Handle: 'invalid library handle',
  FT_Error.Invalid_Driver_Handle: 'invalid module handle',
  FT_Error.Invalid_Face_Handle: 'invalid face handle',
  FT_Error.Invalid_Size_Handle: 'invalid size handle',
  FT_Error.Invalid_Slot_Handle: 'invalid glyph slot handle',
  FT_Error.Invalid_CharMap_Handle: 'invalid charmap handle',
  FT_Error.Invalid_Cache_Handle: 'invalid cache manager handle',
  FT_Error.Invalid_Stream_Handle: 'invalid stream handle',
  FT_Error.Too_Many_Drivers: 'too many modules',
  FT_Error.Too_Many_Extensions: 'too many extensions',
  FT_Error.Out_Of_Memory: 'out of memory',
  FT_Error.Unlisted_Object: 'unlisted object',
  FT_Error.Cannot_Open_Stream: 'cannot open stream',
  FT_Error.Invalid_Stream_Seek: 'invalid stream seek',
  FT_Error.Invalid_Stream_Skip: 'invalid stream skip',
  FT_Error.Invalid_Stream_Read: 'invalid stream read',
  FT_Error.Invalid_Stream_Operation: 'invalid stream operation',
  FT_Error.Invalid_Frame_Operation: 'invalid frame operation',
  FT_Error.Nested_Frame_Access: 'nested frame access',
  FT_Error.Invalid_Frame_Read: 'invalid frame read',
  FT_Error.Raster_Uninitialized: 'raster uninitialized',
  FT_Error.Raster_Corrupted: 'raster corrupted',
  FT_Error.Raster_Overflow: 'raster overflow',
  FT_Error.Raster_Negative_Height: 'negative height while rastering',
  FT_Error.Too_Many_Caches: 'too many registered caches',
  FT_Error.Invalid_Opcode: 'invalid opcode',
  FT_Error.Too_Few_Arguments: 'too few arguments',
  FT_Error.Stack_Overflow: 'stack overflow',
  FT_Error.Code_Overflow: 'code overflow',
  FT_Error.Bad_Argument: 'bad argument',
  FT_Error.Divide_By_Zero: 'division by zero',
  FT_Error.Invalid_Reference: 'invalid reference',
  FT_Error.Debug_OpCode: 'found debug opcode',
  FT_Error.ENDF_In_Exec_Stream: 'found ENDF opcode in execution stream',
  FT_Error.Nested_DEFS: 'nested DEFS',
  FT_Error.Invalid_CodeRange: 'invalid code range',
  FT_Error.Execution_Too_Long: 'execution context too long',
  FT_Error.Too_Many_Function_Defs: 'too many function definitions',
  FT_Error.Too_Many_Instruction_Defs: 'too many instruction definitions',
  FT_Error.Table_Missing: 'SFNT font table missing',
  FT_Error.Horiz_Header_Missing: 'horizontal header (hhea) table missing',
  FT_Error.Locations_Missing: 'locations (loca) table missing',
  FT_Error.Name_Table_Missing: 'name table missing',
  FT_Error.CMap_Table_Missing: 'character map (cmap) table missing',
  FT_Error.Hmtx_Table_Missing: 'horizontal metrics (hmtx) table missing',
  FT_Error.Post_Table_Missing: 'PostScript (post) table missing',
  FT_Error.Invalid_Horiz_Metrics: 'invalid horizontal metrics',
  FT_Error.Invalid_CharMap_Format: 'invalid character map (cmap) format',
  FT_Error.Invalid_PPem: 'invalid ppem value',
  FT_Error.Invalid_Vert_Metrics: 'invalid vertical metrics',
  FT_Error.Could_Not_Find_Context: 'could not find context',
  FT_Error.Invalid_Post_Table_Format: 'invalid PostScript (post) table format',
  FT_Error.Invalid_Post_Table: 'invalid PostScript (post) table',
  FT_Error.DEF_In_Glyf_Bytecode: 'found FDEF or IDEF opcode in glyf bytecode',
  FT_Error.Missing_Bitmap: 'missing bitmap in strike',
  FT_Error.Missing_SVG_Hooks: 'SVG hooks have not been set',
  FT_Error.Syntax_Error: 'opcode syntax error',
  FT_Error.Stack_Underflow: 'argument stack underflow',
  FT_Error.Ignore: 'ignore',
  FT_Error.No_Unicode_Glyph_Name: 'no Unicode glyph name found',
  FT_Error.Glyph_Too_Big: 'glyph too big for hinting',
  FT_Error.Missing_Startfont_Field: "`STARTFONT' field missing",
  FT_Error.Missing_Font_Field: "`FONT' field missing",
  FT_Error.Missing_Size_Field: "`SIZE' field missing",
  FT_Error.Missing_Fontboundingbox_Field: "`FONTBOUNDINGBOX' field missing",
  FT_Error.Missing_Chars_Field: "`CHARS' field missing",
  FT_Error.Missing_Startchar_Field: "`STARTCHAR' field missing",
  FT_Error.Missing_Encoding_Field: "`ENCODING' field missing",
  FT_Error.Missing_Bbx_Field: "`BBX' field missing",
  FT_Error.Bbx_Too_Big: "`BBX' too big",
  FT_Error.Corrupted_Font_Header: 'Font header corrupted or missing fields',
  FT_Error.Corrupted_Font_Glyphs: 'Font glyphs corrupted or missing fields',
}

def _map_err(err: FT_Error):
  if err == FT_Error.Ok:
    return
  raise FreetypeException(_ERR_MAP[err])

def _chk_err(res, func, args):
  _map_err(FT_Error(res))
  return res

_ft_init_freetype = _libfreetype.FT_Init_FreeType
_ft_init_freetype.argtypes = [POINTER(FT_Library)]
_ft_init_freetype.restype = c_int
_ft_init_freetype.errcheck = _chk_err

_ft_done_freetype = _libfreetype.FT_Done_FreeType
_ft_done_freetype.argtypes = [FT_Library]
_ft_done_freetype.restype = c_int
_ft_done_freetype.errcheck = _chk_err

_ft_new_face = _libfreetype.FT_New_Face
_ft_new_face.argtypes = [FT_Library, c_char_p, c_long, POINTER(FT_Face)]
_ft_new_face.restype = c_int
_ft_new_face.errcheck = _chk_err

_ft_done_face = _libfreetype.FT_Done_Face
_ft_done_face.argtypes = [FT_Face]
_ft_done_face.restype = c_int
_ft_done_face.errcheck = _chk_err

def FT_Init_FreeType() -> FT_Library:
  alibrary = FT_Library()
  _ft_init_freetype(byref(alibrary))
  finalize(alibrary, lambda x: _ft_done_freetype(FT_Library(x)), alibrary.value)
  return alibrary

_DEPS: dict[int, Any] = {}

def _finalize_with_dep(obj: Any, dep: Any, cb, *args):
  id_ = id(obj)
  _DEPS[id_] = dep

  def inner():
    cb(*args)
    del _DEPS[id_]

  finalize(obj, inner)

def FT_New_Face(library: FT_Library, filepathname: str, face_index: int) -> FT_Face:
  aface = FT_Face()
  _ft_new_face(library, filepathname.encode(), face_index, byref(aface))
  _finalize_with_dep(aface, library, lambda x: _ft_done_face(FT_Face(FT_FaceRec.from_address(x))), addressof(aface.contents))
  return aface
