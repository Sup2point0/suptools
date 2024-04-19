'''
Implements the `Script` class for running scripts with status messages.
'''

from typing import Callable

from .logging import log


def run(script: Callable):
  '''Run a script with status messages when execution starts and ends.'''
  
  log(status = "Running!")
  script()
  log(status = "Done!")
