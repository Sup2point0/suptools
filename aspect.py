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
