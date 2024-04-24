import itertools as it
import json
from base64 import b64decode
from io import StringIO
from typing import Callable


def save_json(file, data: dict) -> None:
  '''Save data to a JSON file.'''

  file.write(json.dumps(data, indent = 2))


def restructure_json(file, indent = 2) -> None:
  '''Reformat contents of `file`.'''

  data = json.load(file)
  content = json.dumps(data, indent = indent)
  file.write(content)


def decode_base64_lines(
  content: str,
  chunksize = 20,
  lines: int = None,
  predicate: Callable = None
) -> str:
  '''Decode a base64 string in chunks and split it into lines.
  
  When either `lines` have been returned or `predicate()` returns a truthy value, the generator returns its last value and stops.
  
  This is significantly safer than `.split()` or other bulk-processing methods, since it avoids parsing all of the content at once, only when needed.
  '''

  batches = it.batched(content, chunksize)
  decoded = StringIO()
  
  count = 0
  done = False

  while "there is content left unprocessed":
    count += 1

    while "no newline reached":
      try:
        batch = next(batches)
      except StopIteration:
        return
      
      chunk = b64decode(batch).decode("utf-8")
      last, _, overflow = chunk.partition("\n")

      decoded.write(last)
      if overflow:
        break

    if lines is not None:
      if count > lines:
        done = True
    if predicate:
      if predicate():
        done = True
    
    line = out.getvalue()
    decoded = StringIO(overflow)

    if done:
      return line
    else:
      yield line
