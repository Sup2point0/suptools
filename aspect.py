# functions involving text


import json

from textwrap import dedent


def ground(content: str) -> str:
  '''Remove common indentation from text, and strip leading and trailing whitespace.
  
  ```py
  >>> s = """
          sup
        suppety
          sup
  """
  >>> print(ground(s))
    sup
  suppety
    sup
  ```
  '''
  
  return dedent(content).strip()


def compose(file: str, indent: int = 2) -> None:
  '''Overwrite JSON file with neatly indented text.
  '''
  
  with open(file, "r+") as source:
    content = json.load(source)
    source.seek(0)
    source.write(json.dumps(content, indent = indent))
    source.truncate()
