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
\x00\x00\x04P\
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
\x0a\x0avar animechoNa\
tiveCb = null;\x0a\x0a\
const animechoWe\
bChan = new QWeb\
Channel(qt.webCh\
annelTransport, \
function(channel\
) {\x0a  const anim\
echo = channel.o\
bjects.animecho;\
\x0a\x0a  // calls fro\
m native into we\
b\x0a  animecho.nat\
iveUpdateContent\
.connect(animech\
oUpdateContent)\x0a\
\x0a  // calls from\
 web into native\
\x0a  animechoNativ\
eCb = animecho.n\
otifyNativeCalle\
dback;\x0a\x0a  animec\
ho.notifyNativeL\
oadFinished();\x0a}\
);\x0a\x0aaddEventList\
ener('beforeunlo\
ad', function(ev\
ent) {\x0a  localSt\
orage.setItem(KE\
Y_ANIMECHO_SCROL\
L, scrollY.toStr\
ing());\x0a});\x0a\x0afun\
ction animechoCb\
(lidx, aidx) {\x0a \
 if (animechoNat\
iveCb === null) \
{\x0a    console.er\
ror(\x22native is n\
ot ready\x22);\x0a    \
return;\x0a  }\x0a\x0a  a\
nimechoNativeCb(\
lidx, aidx);\x0a}\x0a\
\x00\x00\x00\xac\
b\
ody {\x0a  font-siz\
e: 125%;\x0a  user-\
select: none;\x0a}\x0a\
\x0ahtml {\x0a  /* for\
 fade-in */\x0a  tr\
ansition: opacit\
y 800ms ease;\x0a  \
opacity: 0;\x0a}\x0a\x0a.\
animecho-unfinis\
hed {\x0a  cursor: \
pointer;\x0a}\x0a\
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
\x00\x00\x00R\x00\x00\x00\x00\x00\x01\x00\x00\x05\xd3\
\x00\x00\x01\x9e\x8e\xc7\x99q\
\x00\x00\x006\x00\x00\x00\x00\x00\x01\x00\x00\x01\x7f\
\x00\x00\x01\x9e\x8e\xa3{\xc9\
\x00\x00\x00\x16\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9e\x8dv<k\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
