'''
Implements the `Script` class for running scripts with status messages.
'''

from typing import Callable

from . import vitality
from .logging import log


def run(script: Callable, vitals = True):
  '''Run a script with status messages when execution starts and ends.'''
  
  log(status = "Running!")

  if vitals:
    if not hasattr(script, "vitals"):
      script = vitality.vitals(view = True)(script)
  
  out = script()
  
  for vital in vitality.VIEWS:
    if vital.runs:
      print(vital.view())
  
  log(status = "Done!")
  return out
