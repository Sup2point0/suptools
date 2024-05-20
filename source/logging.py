'''
Stylised printing.
'''

LINES = "-" * 42

WHITE = "\033[0m"
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
    print(f"\n{LINES} {status} {LINES}\n{WHITE}")
  if act:
    print(f">> {CYAN}{act}{WHITE}")
  if text:
    print(f"{text}{WHITE}")
  for key, val in kwargs.items():
    print(f"|| {BLUE}{key}{WHITE} = {val}{WHITE}")
  if error:
    print(f"|> {RED}{error}{WHITE}")

def _log_(content: str):
  print(content + WHITE)


def _input_(text: str) -> str:
  '''Prompt the user for input.'''

  return input("=> text = ")
