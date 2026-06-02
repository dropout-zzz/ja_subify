const animechoRoot = document.getElementById('animecho-root');

const animechoWebChan = new QWebChannel(qt.webChannelTransport, function(channel) {
  const animecho = channel.objects.animecho;

  animecho.notifyNativeLoadFinished();
});
