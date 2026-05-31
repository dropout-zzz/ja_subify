ja_subify
=========

## Documentation

### Blacklisting words

It is not desirable to always show every furigana or romanized loan words.

The HTML renderer allows you to specify a local user dictionary file.

The renderer will skip known words and readings that is present in the blacklist files.

Note that for kanji words, if part of the word with same pronunciation exists in database, labeling is also skipped, even if the exact full word is not in the dictionary.
