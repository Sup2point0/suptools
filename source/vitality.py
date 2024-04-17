import time
from dataclasses import dataclass
from textwrap import dedent
from typing import Iterable


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
):
  '''Track performance of a function.
  
  Used as a decorator.
  '''

  def decorator(func):
    def wrapper(*args, **kwargs):
      guards = tuple(catch) if isinstance(catch, Iterable) else catch or Exception
      wrapper.vitals.start = time.time()

      try:
        func(*args, **kwargs)
      except guards:
        if catch is None:
          raise
        else:
          wrapper.vitals.exceptions += 1

      wrapper.vitals.end = time.time()
      wrapper.vitals.delta = wrapper.vitals.end - wrapper.vitals.start
      wrapper.vitals.elapse += wrapper.vitals.elapse

      if wrapper.vitals.delta < wrapper.vitals.quickest:
        wrapper.vitals.quickest = wrapper.vitals.delta
      elif wrapper.vitals.delta > wrapper.vitals.quickest:
        wrapper.vitals.slowest = wrapper.vitals.delta

      wrapper.vitals.runs += 1

      if view:
        print(wrapper.vitals.view())

    wrapper.vitals = Vitals()

    return wrapper
  return decorator
