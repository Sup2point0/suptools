import itertools as it
import json
from base64 import standard_b64decode
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


def isplitlines_base64(
  content: str,
  chunksize = 20,
  lines: int = None,
  predicate: Callable = None
) -> str:
  '''Decode a base64 string in chunks and split it into lines. The generator stops when either `lines` have been returned or `predicate()` returns a truthy value.
  
  This is significantly safer than `.split()` or other bulk-processing methods, since it avoids parsing all of the content at once, only when needed.
  '''

  batches = it.batched(content, chunksize)

  out = StringIO()
  decoded = StringIO()

  i = -1
  count = 0

  while "there is content left unprocessed":
    i += 1

    try:
      char = decoded[i]
    except IndexError:
      try:
        batch = next(batches)
      except StopIteration:
        break
      
      chunk = standard_b64decode(batch)
      decoded.write(chunk)
      char = decoded[i]
    
    out.write(char)

    count += 1
    if lines is not None and count > lines:
      break
    elif (predicate or (lambda: False))():
      break
    else:
      line = out.getvalue()
      out = StringIO()
      yield line
