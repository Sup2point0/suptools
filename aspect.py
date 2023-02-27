# functions involving text


import json

from textwrap import dedent


def assort(content, sep: str = ". ", *, line: str = "\n") -> str:
  '''Arrange items of an iterable in a numbered list.
  
  ```py
  >>> l = [sup, nova, shard]
  >>> print(assort(l))
  1. sup
  2. nova
  3. shard
  ```
  '''
  
  return line.join(f"{i + 1}{sep}{item}" for i, item in enumerate(content))


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
