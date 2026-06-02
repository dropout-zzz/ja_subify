# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.10.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x01F\
<\
!doctype html>\x0a<\
html lang=\x22ja\x22>\x0a\
  <head>\x0a    <me\
ta charset=\x22utf-\
8\x22/>\x0a    <link h\
ref=\x22qrc:///anim\
echo/animecho.cs\
s\x22 rel=\x22styleshe\
et\x22/>\x0a  </head>\x0a\
  <body>\x0a    <di\
v id=\x22animecho-r\
oot\x22></div>\x0a    \
<script src=\x22qrc\
:///qtwebchannel\
/qwebchannel.js\x22\
></script>\x0a    <\
script src=\x22qrc:\
///animecho/anim\
echo.js\x22></scrip\
t>\x0a  </body>\x0a</h\
tml>\x0a\
\x00\x00\x01q\
c\
onst animechoRoo\
t = document.get\
ElementById('ani\
mecho-root');\x0a\x0af\
unction animecho\
UpdateContent(s)\
 {\x0a  animechoRoo\
t.innerHTML = s;\
\x0a}\x0a\x0aconst animec\
hoWebChan = new \
QWebChannel(qt.w\
ebChannelTranspo\
rt, function(cha\
nnel) {\x0a  const \
animecho = chann\
el.objects.anime\
cho;\x0a\x0a  animecho\
.nativeUpdateCon\
tent.connect(ani\
mechoUpdateConte\
nt)\x0a\x0a  animecho.\
notifyNativeLoad\
Finished();\x0a});\x0a\
\
\x00\x00\x00\x00\
\
"

qt_resource_name = b"\
\x00\x08\
\x05\x03\xb4\xef\
\x00a\
\x00n\x00i\x00m\x00e\x00c\x00h\x00o\
\x00\x0d\
\x0f\xc4\x8d\xbc\
\x00a\
\x00n\x00i\x00m\x00e\x00c\x00h\x00o\x00.\x00h\x00t\x00m\x00l\
\x00\x0b\
\x0bO\xc5s\
\x00a\
\x00n\x00i\x00m\x00e\x00c\x00h\x00o\x00.\x00j\x00s\
\x00\x0c\
\x04\xfcM\xc3\
\x00a\
\x00n\x00i\x00m\x00e\x00c\x00h\x00o\x00.\x00c\x00s\x00s\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00R\x00\x00\x00\x00\x00\x01\x00\x00\x02\xbf\
\x00\x00\x01\x9e\x8a\x91\xec\xe8\
\x00\x00\x006\x00\x00\x00\x00\x00\x01\x00\x00\x01J\
\x00\x00\x01\x9e\x8az\x16\xe2\
\x00\x00\x00\x16\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9e\x8a\x96\xb6S\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
