from dataclasses import dataclass


@ dataclass(slots = True)
class Version:
  '''A lightweight representation of a 3-value version number.'''

  root: int = 1
  major: int = 0
  minor: int = 0
  dev: str = ""

  def __post_init__(self):
    if isinstance(self.root, str):
      parts = self.root.split(".")

      self.root = int(parts.pop(0))
      if parts:
        self.major = int(parts.pop(0))
      if parts:
        self.minor = int(parts.pop(0))
      if parts:
        self.dev = ".".join(parts)

  def update(self, part: str) -> Version:
    '''Increment the version.'''

    match part:
      case "root":
        self.root += 1
        self.major = 0
        self.minor = 0

      case "major":
        self.major += 1
        self.minor = 0

      case "minor":
        self.minor += 1
