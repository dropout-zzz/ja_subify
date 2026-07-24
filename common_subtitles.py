from dataclasses import dataclass

@dataclass
class Subtitle:
  text: str
  timing: tuple[int, int]
