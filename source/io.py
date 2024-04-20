import json


def save_json(file, data: dict):
  '''Save data to a JSON file.'''

  file.write(json.dumps(data, indent = 2))


def restructure_json(file, indent = 2):
  '''Reformat contents of `file`.'''

  data = json.load(file)
  content = json.dumps(data, indent = indent)
  file.write(content)
