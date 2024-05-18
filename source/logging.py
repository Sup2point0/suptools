'''
Stylised printing.
'''

LINES = "-" * 42

BLUE = "\033[94m"
CYAN = "\033[96m"
RED = "\033[93m"


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
    print(f"{CYAN}>> {act}")
  if text:
    print(text)
  for key, val in kwargs.items():
    print(f"{BLUE}|| {key} = {val}")
  if error:
    print(f"{RED}|> {error}")


def _input_(text: str) -> str:
  '''Prompt the user for input.'''

  return input("=> text = ")
