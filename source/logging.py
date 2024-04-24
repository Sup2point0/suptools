'''
Stylised printing.
'''

LINES = "-" * 42


def log(
  text: str = None,
  status: str = None,
  act: str = None,
  error: Exception = None,
  **kwargs,
):
  '''Print something.'''

  if status:
    print(f"\n{LINES} {status} {LINES}\n")
  if act:
    print(f">> {act}")
  if text:
    print(text)
  for key, val in kwargs.items():
    print(f"|| {key} = {val}")
  if error:
    print(f"|> {error}")


def _input_(text: str) -> str:
  '''Prompt the user for input.'''

  return input("=> text = ")
