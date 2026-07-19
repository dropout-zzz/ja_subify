ja_subify
=========

![](https://img.shields.io/github/repo-size/dropout-zzz/ja_subify?style=for-the-badge)

Tools to convert untranslated Japanese anime subtitles into text documents, quickly add Furigana to them and render as HTML.

In future, rendering as ASS subtitle may be supported.

## Quick start

1. Ensure Python and PySide6 (optional, for GUIs) is installed on system.

2. Simply start program files.

## Documentation

### Blacklisting words

It is not desirable to always show every furigana or romanized loan words.

The HTML renderer allows you to specify a local user dictionary file. It is recommended to use one.

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
