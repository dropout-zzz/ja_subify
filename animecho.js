const KEY_ANIMECHO_SCROLL = 'animecho_scroll';

const animechoRoot = document.getElementById('animecho-root');

function animechoUpdateContent(s, restore_scroll) {
  animechoRoot.innerHTML = s;

  if (restore_scroll) {
    const saved_scroll = localStorage.getItem(KEY_ANIMECHO_SCROLL);

    if (saved_scroll !== null)
      scrollTo(0, parseInt(saved_scroll, 10));
  }

  // fade-in
  document.documentElement.style.opacity = '1';
}

const animechoWebChan = new QWebChannel(qt.webChannelTransport, function(channel) {
  const animecho = channel.objects.animecho;

  animecho.nativeUpdateContent.connect(animechoUpdateContent)

  animecho.notifyNativeLoadFinished();
});

addEventListener('beforeunload', function(event) {
  localStorage.setItem(KEY_ANIMECHO_SCROLL, scrollY.toString());
});
