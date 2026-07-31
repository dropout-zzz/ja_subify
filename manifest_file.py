"""Manifest File is a simple list keeping information for
   loading multiple .annotations files.
   as we want to re-use things like lyrics many times,
   we only need to store them in a separate .annotations file and
    keep an offset where the template should be placed at.

   in Manifest File, each line is two string separated by a space:
    the offset in seconds (a floating point number), and
    file name of the .annotations without the extension.
    (the file will be looked for in same directory with the .manifest file.)

   if any dialogue line is overlapped, manifest loader always drops the
    previous conflicting lines, guaranteeing all lines in the
    last file mentioned in the .manifest file are always retained.

   it's recommended that you write the shorter Annotation File at last,
    because overlap detection is currently expensive."""

from dataclasses import dataclass
import dataclasses
from annotation_file import AnnotationFile, annotation_parse
from os.path import realpath, dirname
import os.path

@dataclass
class Manifest:
  # Annotation Files stored in this list are already offseted.
  afs: list[AnnotationFile] = dataclasses.field(default_factory=list)

def manifest_load(path: str) -> Manifest:
  """load Annotation Files listed by a Manifest File stored at `path'."""

  mf = Manifest()
  basedir = dirname(realpath(path))

  with open(path, 'r') as f:
    for s in f:
      s_offset, s_basename = s.removesuffix('\n').split(maxsplit=1)

      # AF uses milliseconds. convert into it.
      offset = int(float(s_offset) * 1000)

      with open(os.path.join(basedir, f'{s_basename}.annotations'), 'r') as f2:
        new_af = annotation_parse(f2.read())

      for new_dialogue in new_af.lines:
        # retime the template
        new_dialogue.start_time += offset
        new_dialogue.end_time += offset

        for old_af in mf.afs:
          for i in range(len(old_af.lines) - 1, -1, -1):
            old_dialogue = old_af.lines[i]

            if max(new_dialogue.start_time, old_dialogue.start_time) < min(new_dialogue.end_time, old_dialogue.end_time):
              print(f'manifest loader: dropping overlapped line {old_dialogue.get_normalized()!r}')
              old_af.lines.pop(i)

      mf.afs.append(new_af)

  return mf
