import time
from dataclasses import dataclass
from textwrap import dedent
from typing import Iterable

from .logging import log


VIEWS = []


@ dataclass
class Vitals:
  shard: str = ""
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
      | {self.shard}
      | runs = {self.runs}
      | last delta = {round(self.delta, 4)}
      | quickest = {round(self.quickest, 4)}
      | slowest = {round(self.slowest, 4)}
      | average = {round(self.average, 4)}
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
      vita.elapse += vita.delta

      if vita.delta < vita.quickest:
        vita.quickest = vita.delta
      if vita.delta > vita.slowest:
        vita.slowest = vita.delta

      vita.runs += 1

      return out

    wrapper.vitals = Vitals(shard = repr(func))

    if view:
      VIEWS.append(wrapper.vitals)
    
    return wrapper
  
  return decorator
