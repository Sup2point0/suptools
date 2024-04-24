import time
from dataclasses import dataclass
from textwrap import dedent
from typing import Iterable

from .logging import log


@ dataclass
class Vitals:
  start: float = None
  end: float = None
  delta: float = None
  quickest: float = float("inf")
  slowest: float = float("-inf")
  elapse: float = 0
  runs: int = 0
  exceptions: int = 0

  @ property
  def average(self) -> float:
    return self.elapse / self.runs
  
  def view(self) -> str:
    return dedent(f'''
      --- suptools: vitality ---
      | runs = {self.runs}
      | last delta = {round(self.delta, 2)}
      | quickest = {round(self.quickest, 2)}
      | slowest = {round(self.slowest, 2)}
      | average = {round(self.average, 2)}
    ''')


def vitals(
  catch: Exception | list[Exception] = None,
  view: bool = False,
  track_calls = False,
):
  '''Track performance of a function.
  
  Used as a decorator.
  '''

  def decorator(func):
    def wrapper(*args, **kwargs):
      guards = tuple(catch) if isinstance(catch, Iterable) else catch or Exception

      vita = wrapper.vitals
      vita.start = time.time()

      if track_calls:
        log(act = f"calling {repr(func)}")

      try:
        out = func(*args, **kwargs)
      except guards as e:
        if catch is None:
          raise
        else:
          vita.exceptions += 1
          log(error = e)

      vita.end = time.time()
      vita.delta = vita.end - vita.start
      vita.elapse += vita.elapse

      if vita.delta < vita.quickest:
        vita.quickest = vita.delta
      elif vita.delta > vita.quickest:
        vita.slowest = vita.delta

      vita.runs += 1

      if view:
        print(vita.view())

      return out

    wrapper.vitals = Vitals()

    return wrapper
  return decorator
