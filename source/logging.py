'''
Stylised printing.
'''

LINES = "-" * 42


def log(
  text: str = None,
  status: str = None,
  action: str = None,
  **kwargs,
):
  '''Print something.'''

  if status:
    print(f"\n{LINES} STATUS = {status} {LINES}\n")
  elif action:
    print(f">> {action}")
  elif text:
    print(text)
  else:
    for key, val in kwargs.items():
      print(f"|> {key} = {val}")
