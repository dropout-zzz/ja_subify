const animechoRoot = document.getElementById('animecho-root');

function animechoUpdateContent(s) {
  animechoRoot.innerHTML = s;
}

const animechoWebChan = new QWebChannel(qt.webChannelTransport, function(channel) {
  const animecho = channel.objects.animecho;

  animecho.nativeUpdateContent.connect(animechoUpdateContent)

  animecho.notifyNativeLoadFinished();
});
