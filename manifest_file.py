from dataclasses import dataclass
import dataclasses
from annotation_file import AnnotationFile

@dataclass
class Manifest:
  afs: list[AnnotationFile] = dataclasses.field(default_factory=list)

def manifest_load(path: str) -> Manifest:
  mf = Manifest()

  return mf
