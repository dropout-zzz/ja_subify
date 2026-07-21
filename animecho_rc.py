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
\x00\x00\x08+\
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
oll === null)\x0a  \
    console.erro\
r(\x22scroll progre\
ss is not alread\
y saved\x22);\x0a    e\
lse\x0a      scroll\
To(0, parseInt(s\
aved_scroll, 10)\
);\x0a  }\x0a\x0a  // fad\
e-in\x0a  document.\
documentElement.\
style.opacity = \
'1';\x0a}\x0a\x0afunction\
 animechoGoToLin\
e(lidx) {\x0a  cons\
t dialogueLine =\
 document.getEle\
mentById(`animec\
ho-l${lidx}`);\x0a\x0a\
  if (dialogueLi\
ne === null) {\x0a \
   console.error\
(\x22cannot get dia\
logue line elem\x22\
);\x0a    return;\x0a \
 }\x0a\x0a  dialogueLi\
ne.scrollIntoVie\
w({ block: \x22cent\
er\x22 });\x0a}\x0a\x0afunct\
ion animechoUpda\
tePartialContent\
(lidx, s) {\x0a  co\
nst dialogueLine\
 = document.getE\
lementById(`anim\
echo-l${lidx}`);\
\x0a\x0a  if (dialogue\
Line === null) {\
\x0a    console.err\
or(\x22cannot get d\
ialogue line ele\
m\x22);\x0a    return;\
\x0a  }\x0a\x0a  dialogue\
Line.innerHTML =\
 s;\x0a}\x0a\x0avar anime\
choNativeCb = nu\
ll;\x0avar animecho\
NativeCb2 = null\
;\x0a\x0aconst animech\
oWebChan = new Q\
WebChannel(qt.we\
bChannelTranspor\
t, function(chan\
nel) {\x0a  const a\
nimecho = channe\
l.objects.animec\
ho;\x0a\x0a  // calls \
from native into\
 web\x0a  animecho.\
nativeUpdateCont\
ent.connect(anim\
echoUpdateConten\
t);\x0a  animecho.n\
ativeGoToLine.co\
nnect(animechoGo\
ToLine);\x0a  anime\
cho.nativeUpdate\
PartialContent.c\
onnect(animechoU\
pdatePartialCont\
ent);\x0a\x0a  // call\
s from web into \
native\x0a  animech\
oNativeCb = anim\
echo.notifyNativ\
eCalledback;\x0a  a\
nimechoNativeCb2\
 = animecho.noti\
fyNativeContextM\
enu;\x0a\x0a  animecho\
.notifyNativeLoa\
dFinished();\x0a});\
\x0a\x0aaddEventListen\
er('beforeunload\
', function(even\
t) {\x0a  localStor\
age.setItem(KEY_\
ANIMECHO_SCROLL,\
 scrollY.toStrin\
g());\x0a});\x0a\x0afunct\
ion animechoCb(l\
idx, aidx) {\x0a  i\
f (animechoNativ\
eCb === null) {\x0a\
    console.erro\
r(\x22native is not\
 ready\x22);\x0a    re\
turn;\x0a  }\x0a\x0a  ani\
mechoNativeCb(li\
dx, aidx);\x0a}\x0a\x0afu\
nction animechoC\
b2(event, lidx) \
{\x0a  event.preven\
tDefault();\x0a\x0a  i\
f (animechoNativ\
eCb2 === null) {\
\x0a    console.err\
or(\x22native is no\
t ready.\x22);\x0a    \
return;\x0a  }\x0a\x0a  a\
nimechoNativeCb2\
(lidx);\x0a}\x0a\
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
\x00\x00\x00R\x00\x00\x00\x00\x00\x01\x00\x00\x09\xac\
\x00\x00\x01\x9f\x7f\xd8\xcb\xc9\
\x00\x00\x006\x00\x00\x00\x00\x00\x01\x00\x00\x01}\
\x00\x00\x01\x9f\x83\xc4\xc9\xb1\
\x00\x00\x00\x16\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9f\x7f\xd8\xcb\xc9\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
