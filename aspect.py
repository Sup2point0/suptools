# functions involving text


import json

from textwrap import dedent


def stylize(content: str, *, quotes = True, dashes = True) -> str:
  '''Stylize text with slanted quotes and full dashes.
  
  If `quotes` is set to:
  `True`: Change all to slanted quote marks.
  `False`: Change all to slanted quote marks.
  `None`: No change.
  
  If `dashes` is set to:
  `True`: Add en and em dashes.
  `False`: Remove all en and em dashes.
  `None`: Do not stylize dashes.
  '''
  
  def style(text: str, ctx: dict):
    for key in ctx:
      if ctx[key]:
        self = text.replace(key, ctx[key])
    return self
  
  if quotes != None:
    if quotes:
      content = style(content, {
        "'": "’",
        "\"": "”",
        " ’": " ‘",
        " ”": " “",
      })
    else:
      content = style(content, {
        "‘": "'",
        "’": "'",
        "“": "\"",
        "”": "\"",
      })
  
  if dashes != None:
    if dashes:
      content = style(content, {
        " - ": " – ",
        " -- ": " – ",
      })
    else:
      content = style(content, {
        "–": "-",
        " — ": " - ",
        "—": "-",
      })
  
  return content


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
