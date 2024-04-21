'''
Implements the `Script` class for running scripts with status messages.
'''

from typing import Callable

from .logging import log
from .vitality import vitals


def run(script: Callable, vitals = True):
  '''Run a script with status messages when execution starts and ends.'''
  
  log(status = "Running!")

  if vitals:
    if not hasattr(script, "vitals"):
      script = vitals(view = True)(script)
  
  return script()
  
  log(status = "Done!")
