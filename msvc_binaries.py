"""on windows we ship native dependencies with the app."""

import os
import sys
import os.path

def get_program_location() -> str:
  # https://pyinstaller.org/en/stable/runtime-information.html
  if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    return os.path.dirname(sys.executable)
  return os.path.dirname(os.path.abspath(__file__))

if os.name == 'nt' and not getattr(sys, '_is_mingw', False):
  # as per Python documentation,
  #  ctypes.util.find_library() searches PATH on Windows.
  os.environ['PATH'] += ';'
  os.environ['PATH'] += os.path.join(get_program_location(), 'msvc_sup', os.environ['PROCESSOR_ARCHITECTURE'])
