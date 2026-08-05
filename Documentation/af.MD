Annotation File is an intermediate representation used throughout ja_subify. In this documentation, "AF" is a short hand referring to it.

You can use the `import_srt` or `import_ass` program to create an Annotation File.

Annotation File can be edited by the `annotation_edit` program, or you can also edit it by hand or using scripts.

The purpose of AF is it can store furigana information (in this documentation, we will refer to "furigana" by the word "label" instead), and a few other metadatas useful for the editor program.

## `import_srt`, `import_ass`

these program can read an existing subtitle file and convert it into an Annotation File.

it can also update timings in an existing Annotation File if the AF was created from the same subtitle file. The use case of this is you can retime the original subtitle using existing softwares, for example, in Aegisub, then you can use the `--retime` option to also update timings in the `.annotations` file that you have already imported previously, without losing your labels. The limitation is the program will check if your AF really appear to come from the same subtitle file. (i.e. If you have inserted, deleted, added or modified contents of dialogues in the original subtitle file, retiming will currently fail.)
