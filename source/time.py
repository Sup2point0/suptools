# functions involving time


def display(s: int):
  '''Display `s` seconds as written time.
  
  ```py
  >>> display(60)
  '1 min'
  >>> display(69420)
  '19h 17 min'
  >>> print(display(31415926), "ago")
  363d 14h ago
  ```
  '''
  
  if s / 86400 >= 1:
    if s // 360 % 360 >= 0:
      return f"{int(s // 86400)}d {int(s // 3600 % 24)}h"
    return f"{int(s // 86400)}d"
  elif s / 60 >= 60:
    if s // 60 % 60 > 0:
      return f"{int(s // 3600)}h {int(s // 60 % 60)} min"
    return f"{int(s // 3600)}h"
  elif s >= 60:
    return f"{int(s // 60)} min"
  else:
    return "a few seconds"
