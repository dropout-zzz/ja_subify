ja_subify
=========

![](https://img.shields.io/github/repo-size/dropout-zzz/ja_subify?style=for-the-badge)

Tools to convert untranslated Japanese anime subtitles into text documents, quickly add Furigana to them and render as HTML or `.ass`.

## Samples

Some anime subtitles are annotated and the rendered HTML/ASS results are provided in this repo for learning purposes. They can be used standalone.

These subtitles are timed to BD and require a player with libass renderer (e.g. MPV, VLC or IINA) to work properly.

Subtitles are also font-dependent, the samples use `Noto Sans CJK JP` (which should be installed on most recent Linux and Android systems). If needed, install the font if it's missing or run the renderer script yourself and change the font family using CLI option.

However, if you can, it's probably more recommended to use `Rounded M+ 1p` as it's closer to idiomatic choice for Japanese anime subtitles.

## Quick start

1. Ensure Python and PySide6 (optional, for GUIs) is installed on system.

2. Simply start program files.

This software was developed upon the archlinux environment. It's also been tested to work on Windows. Other platforms weren't fully tested as the time of writing.

Android users: [Termux](https://termux.dev/) is your friend (technically), [TUR](https://github.com/termux-user-repository/tur) might useful too.

On macOS, try [Homebrew](https://brew.sh/) or [MacPorts](https://www.macports.org/).

## Documentation

### Blacklisting words

It is not desirable to always show every furigana or romanized loan words.

The HTML/ASS renderer allows you to specify a local user dictionary file. It is recommended to use one.

The renderer will skip known words and readings that is present in the blacklist files.

Note that for kanji words, if part of the word with same pronunciation exists in database, labeling is also skipped, even if the exact full word is not in the dictionary.

## FAQ

### How to undo?

No undo feature yet, fully close all running programs and you can remove items from dictionary files.

To delete labels in editor, right click a line and select "Return to unfinished".

Git is recommended if you want to manage revisions of your files.

## Support

Contact via https://t.me/+Ar9L2FU3kF1lNzY0

## License

ja_subify is *free software*.

A copy of GLWTPL is included.
