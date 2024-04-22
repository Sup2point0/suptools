'''
Stylised printing.
'''

LINES = "-" * 42


def log(
  text: str = None,
  status: str = None,
  act: str = None,
  **kwargs,
):
  '''Print something.'''

  if status:
    print(f"\n{LINES} {status} {LINES}\n")
  elif act:
    print(f">> {act}")
  elif text:
    print(text)
  else:
    for key, val in kwargs.items():
      print(f"|> {key} = {val}")


def _input_(text: str) -> str:
  '''Prompt the user for input.'''

  return input("=> text = ")
