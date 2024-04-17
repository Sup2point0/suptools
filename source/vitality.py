import time
from dataclasses import dataclass


@ dataclass
class Vitals:
  start: float = None
  end: float = None
  delta: float = None
  quickest: float = float("inf")
  slowest: float = float("-inf")
  elapse: float = 0
  runs: int = 0

  @ property
  def average(self) -> float:
    return self.elapse / self.runs


def vitals(
  catch: Exception | list[Exception] = None,
):
  '''Track performance of a function.
  
  Used as a decorator.
  '''

  def decorator(func):
    func.vitals = Vitals()

    def wrapper():
      func.vitals.start = time.time()

      func()

      func.vitals.end = time.time()
      func.vitals.delta = func.vitals.end - func.vitals.start
      func.vitals.elapse += func.vitals.elapse

      if func.vitals.delta < func.vitals.quickest:
        func.vitals.quickest = func.vitals.delta
      elif func.vitals.delta > func.vitals.quickest:
        func.vitals.slowest = func.vitals.delta

      func.vitals.runs += 1

  return decorator
