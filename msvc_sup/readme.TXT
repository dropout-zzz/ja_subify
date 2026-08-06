this directory contains precompiled DLL files that ja_subify needs for
 whoever running on Windows with a MSVC Python. these files won't be
 used by ja_subify when running with Msys2's MinGW Python.

it's only used when you use the ASS renderer program.
it also does nothing if you're not on Windows.

ja_subify uses FreeType library to read a few properties (EM size and
 ascender/descender sizes in OS/2 table) in font files and uses
 Fontconfig library to locate system font files by their names.

(libexpat.dll is a dependency of fontconfig.dll.)

files are provided as a handy option for people who are not willing to
 compile them or find and install these libraries separately.

these binaries was compiled using MSVC compiler that comes with Visual Studio.
the source code for Fontconfig can be found at:
https://github.com/dropout-zzz/fontconfig

(sources codes for other libraries are not special and can be found on Internet.)

for more information, if you want to build these yourself,
 reading this Gist writeup should help:
https://gist.github.com/dropout-zzz/5711fc0e4a487200ed7f7916b03bb5e1
