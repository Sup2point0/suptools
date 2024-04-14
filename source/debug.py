class Debugging:
  '''Access functions for logging data for debugging.'''

  def __init__(self, path = "debug", autosave = True, format = "md"):
    self.path = path
    self.autosave = autosave
    self.format = "md"

    self.started = False
    self.frame = 0
    self.data = []

    self._frame_data = {}
    self._cols = ["index"]

    with open(f"{self.path}.{self.format}", "w+") as file:
      file.seek(0)
      file.truncate()

  def log(self, **kwargs):      
    '''Log any number of attributes.
    
    ```py
    >>> debug = Debugging()
    >>> debug.log(sup = 2.0)
    >>> debug.log(nova = True, shard = "bot")
    ```
    '''

    for key, val in kwargs.items():
      self._frame_data[key] = val

      if not self.started:
        self._cols.append(key)

  def save(self):
    '''...'''

    if not self.started:
      self._write_(self._cols)
      self.started = True

    self.data = list(self._frame_data.values())
    self._write_([self.frame] + self.data)

    self.data.clear()
    self._frame_data.clear()

  def _write_(self, data):
    '''...'''

    with open(f"{self.path}.{self.format}", "a") as file:
      match self.format:
        case "md":
          file.write(
            "|" + " | ".join(
              repr(each) for each in data
            ) + " |\n"
          )
          
          if not self.started:
            file.write("|" +
              " | ".join(
                ":" + "-" * (len(each) - 1)
                for each in self._cols
              )
              + " |\n"
            )
        case "csv":
          file.write(", ".join(repr(each) for each in data) + "\n")
