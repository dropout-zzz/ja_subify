For general information of Manifest File (its purpose, format and behavior notes), please read the leading comments in [manifest_file.py](../manifest_file.py).

## one example usage of Manifest File

let's say you have an anime where each episode have the same opening and ending songs.

load NCOP ("No-credits opening", find it in your torrents) and NCED in Aegisub and time them, then sub them (you can copy lyrics from sites like utaten or uta-net).

now import them as two `.annotations` and add labels to them using `annotation_edit`.

for each episode you want a manifest like this:

```
0.0 epXY
123.456 ncop
1234.567 nced
```

this assume you stored AF for that episode at `epXY.annotations` (which doesnt have opening/ending lyrics) and opening lyrics at `ncop.annotations` then `nced.annotations` for ending lyrics

figure out the offset by opening each episode in Aegisub and time the first sentence of opening and ending songs, then minus the time of first sentence in NCOP/NCED.

Currently, ja_subify only support trivial cases like this. But some animes may change playback speeds dynamically in theme songs, which would require a bit more complicated solution.

If you don't have a separate copy of NCOP or NCED video file, use your favourite tool and clip the theme songs regions from any episode and use it. The overall theory should be the same.
