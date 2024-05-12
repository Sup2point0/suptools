import itertools
import json
from base64 import b64decode
from io import StringIO
from typing import Generator, Callable

### NOTE temporary until Python 3.12 works
from .iterate import chunked
itertools.batched = chunked


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
) -> Generator[str, None, None]:
  '''Decode a base64 string in chunks and split it into lines.
  
  When either `lines` have been returned or `predicate()` returns a truthy value, the generator returns its last value and stops.
  
  This is significantly safer than `.split()` or other bulk-processing methods, since it avoids parsing all of the content at once, only when needed.
  '''

  batches = itertools.batched(content, chunksize)
  batch: bytes
  chunk: str
  decoded: str
  stream = ""#StringIO()
  
  count = 0
  done = False

  while True:
    count += 1
    if lines is not None:
      if count > lines:
        done = True

    while True:
      chunk, _, overflow = stream.partition("\n")
      if not overflow:
        try:
          batch = bytes(next(batches))
        except StopIteration:
          done = True
        else:
          decoded = b64decode(batch.decode("utf-8")).decode()
          stream += decoded
          chunk, _, overflow = stream.partition("\n")

      if overflow or done:
        break

    if predicate:
      if predicate():
        done = True
    
    line = chunk
    stream = overflow
    chunk = ""

    if done:
      yield line
      return
    else:
      yield line
