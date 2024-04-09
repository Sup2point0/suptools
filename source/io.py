import json

def overwrite(file, content: str):
  '''Overwrite contents of `file` with `content`.'''

  file.seek(0)
  file.write(content)
  file.truncate()
