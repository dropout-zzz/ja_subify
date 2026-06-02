# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.10.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x01\x05\
<\
!doctype html>\x0a<\
html lang=\x22ja\x22>\x0a\
  <head>\x0a    <me\
ta charset=\x22utf-\
8\x22/>\x0a  </head>\x0a \
 <body>\x0a    <div\
 id=\x22animecho-ro\
ot\x22></div>\x0a    <\
script src=\x22qrc:\
///qtwebchannel/\
qwebchannel.js\x22>\
</script>\x0a    <s\
cript src=\x22qrc:/\
//animecho/anime\
cho.js\x22></script\
>\x0a  </body>\x0a</ht\
ml>\x0a\
\x00\x00\x00\xed\
c\
onst animechoRoo\
t = document.get\
ElementById('ani\
mecho-root');\x0a\x0ac\
onst animechoWeb\
Chan = new QWebC\
hannel(qt.webCha\
nnelTransport, f\
unction(channel)\
 {\x0a  const anime\
cho = channel.ob\
jects.animecho;\x0a\
\x0a  animecho.noti\
fyNativeLoadFini\
shed();\x0a});\x0a\
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
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x006\x00\x00\x00\x00\x00\x01\x00\x00\x01\x09\
\x00\x00\x01\x9e\x89%\xdc\x11\
\x00\x00\x00\x16\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9e\x88\xcb\x14\x8d\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
