# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.10.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x01y\
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
  <ol id=\x22animec\
ho-root\x22></ol>\x0a \
   <script src=\x22\
qrc:///qtwebchan\
nel/qwebchannel.\
js\x22></script>\x0a  \
  <script src=\x22q\
rc:///animecho/a\
nimecho.js\x22></sc\
ript>\x0a  </body>\x0a\
</html>\x0a\
\x00\x00\x04\xec\
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
\x0a\x0afunction anime\
choGoToLine(lidx\
) {\x0a  document.g\
etElementById(`a\
nimecho-l${lidx}\
`).scrollIntoVie\
w();\x0a}\x0a\x0avar anim\
echoNativeCb = n\
ull;\x0a\x0aconst anim\
echoWebChan = ne\
w QWebChannel(qt\
.webChannelTrans\
port, function(c\
hannel) {\x0a  cons\
t animecho = cha\
nnel.objects.ani\
mecho;\x0a\x0a  // cal\
ls from native i\
nto web\x0a  animec\
ho.nativeUpdateC\
ontent.connect(a\
nimechoUpdateCon\
tent);\x0a  animech\
o.nativeGoToLine\
.connect(animech\
oGoToLine);\x0a\x0a  /\
/ calls from web\
 into native\x0a  a\
nimechoNativeCb \
= animecho.notif\
yNativeCalledbac\
k;\x0a\x0a  animecho.n\
otifyNativeLoadF\
inished();\x0a});\x0a\x0a\
addEventListener\
('beforeunload',\
 function(event)\
 {\x0a  localStorag\
e.setItem(KEY_AN\
IMECHO_SCROLL, s\
crollY.toString(\
));\x0a});\x0a\x0afunctio\
n animechoCb(lid\
x, aidx) {\x0a  if \
(animechoNativeC\
b === null) {\x0a  \
  console.error(\
\x22native is not r\
eady\x22);\x0a    retu\
rn;\x0a  }\x0a\x0a  anime\
choNativeCb(lidx\
, aidx);\x0a}\x0a\
\x00\x00\x01\x7f\
b\
ody {\x0a  font-siz\
e: 125%;\x0a  user-\
select: none;\x0a  \
margin: 1rem;\x0a}\x0a\
\x0ahtml {\x0a  /* for\
 fade-in */\x0a  tr\
ansition: opacit\
y 800ms ease;\x0a  \
opacity: 0;\x0a}\x0a\x0a.\
animecho-unfinis\
hed {\x0a  cursor: \
pointer;\x0a}\x0a\x0a.ani\
mecho-ignore {\x0a \
 color: grey;\x0a}\x0a\
\x0a.animecho-loan \
{\x0a  color: blue;\
\x0a}\x0a\x0a.animecho-ka\
nji {\x0a  color: r\
ed;\x0a}\x0a\x0a.animecho\
-line::marker {\x0a\
  color: purple;\
\x0a}\x0a\x0a.animecho-li\
ne {\x0a  margin-bo\
ttom: 1rem;\x0a}\x0a\
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
\x00\x00\x00R\x00\x00\x00\x00\x00\x01\x00\x00\x06m\
\x00\x00\x01\x9e\x95\xbf\x18\x09\
\x00\x00\x006\x00\x00\x00\x00\x00\x01\x00\x00\x01}\
\x00\x00\x01\x9e\x95\x94\xf0S\
\x00\x00\x00\x16\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9e\x95\xb2\x84\xa3\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
