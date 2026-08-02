"""this makes the project work under Msys2."""

import os
import sys

DLL_ABI_VERS = {
  'fontconfig': 1,
  'freetype': 6,
}

def fixup_dll_name(s: str) -> str:
  # it seems Msys2 downstream has introduced this attribute for internal uses
  if os.name == 'nt' and hasattr(sys, '_is_mingw') and sys._is_mingw:
    # we want to use MinGW libraries which uses the "lib" prefix.
    # also, add ABI explictly because it isn't searched automatically.
    # (and there isnt a symlink unlike on Linux distros.)
    return f'lib{s}-{DLL_ABI_VERS[s]}'

  # no-op on other platforms
  return s
