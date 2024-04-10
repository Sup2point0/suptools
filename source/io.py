import json


def overwrite(file, content: str):
  '''Overwrite contents of `file` with `content`.'''

  file.seek(0)
  file.write(content)
  file.truncate()


def restructure_json(file, indent = 2):
  '''Reformat contents of `file`.'''

  data = json.load(file)
  content = json.dumps(data, indent = indent)
  overwrite(file, content)
