# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.10.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x01{\
<\
!doctype html>\x0a<\
html lang=\x22ja\x22>\x0a\
  <head>\x0a    <me\
ta charset=\x22utf-\
8\x22/>\x0a    <meta n\
ame=\x22color-schem\
e\x22 content=\x22ligh\
t dark\x22/>\x0a    <l\
ink href=\x22qrc://\
/animecho/animec\
ho.css\x22 rel=\x22sty\
lesheet\x22/>\x0a  </h\
ead>\x0a  <body>\x0a  \
  <div id=\x22anime\
cho-root\x22></div>\
\x0a    <script src\
=\x22qrc:///qtwebch\
annel/qwebchanne\
l.js\x22></script>\x0a\
    <script src=\
\x22qrc:///animecho\
/animecho.js\x22></\
script>\x0a  </body\
>\x0a</html>\x0a\
\x00\x00\x03\x18\
c\
onst KEY_ANIMECH\
O_SCROLL = 'anim\
echo_scroll';\x0a\x0ac\
onst animechoRoo\
t = document.get\
ElementById('ani\
mecho-root');\x0a\x0af\
unction animecho\
UpdateContent(s,\
 restore_scroll)\
 {\x0a  animechoRoo\
t.innerHTML = s;\
\x0a\x0a  if (restore_\
scroll) {\x0a    co\
nst saved_scroll\
 = localStorage.\
getItem(KEY_ANIM\
ECHO_SCROLL);\x0a\x0a \
   if (saved_scr\
oll !== null)\x0a  \
    scrollTo(0, \
parseInt(saved_s\
croll, 10));\x0a  }\
\x0a\x0a  // fade-in\x0a \
 document.docume\
ntElement.style.\
opacity = '1';\x0a}\
\x0a\x0aconst animecho\
WebChan = new QW\
ebChannel(qt.web\
ChannelTransport\
, function(chann\
el) {\x0a  const an\
imecho = channel\
.objects.animech\
o;\x0a\x0a  animecho.n\
ativeUpdateConte\
nt.connect(anime\
choUpdateContent\
)\x0a\x0a  animecho.no\
tifyNativeLoadFi\
nished();\x0a});\x0a\x0aa\
ddEventListener(\
'beforeunload', \
function(event) \
{\x0a  localStorage\
.setItem(KEY_ANI\
MECHO_SCROLL, sc\
rollY.toString()\
);\x0a});\x0a\
\x00\x00\x00j\
b\
ody {\x0a  font-siz\
e: 125%;\x0a}\x0a\x0ahtml\
 {\x0a  /* for fade\
-in */\x0a  transit\
ion: opacity 800\
ms ease;\x0a  opaci\
ty: 0;\x0a}\x0a\
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
\x00\x00\x00R\x00\x00\x00\x00\x00\x01\x00\x00\x04\x9b\
\x00\x00\x01\x9e\x8d\xd1n\x91\
\x00\x00\x006\x00\x00\x00\x00\x00\x01\x00\x00\x01\x7f\
\x00\x00\x01\x9e\x8d\xd0.\xf4\
\x00\x00\x00\x16\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9e\x8dv<k\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
