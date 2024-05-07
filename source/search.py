'''
Functions for searching iterables.
'''


class NotFound(Exception):
  '''Exception raised when a search does not find the target value.'''


def _search_(source: dict, target, index):
  for key in source:
    val = source[key]
    if key == target:
      return val
    
    if isinstance(val, dict):
      try:
        out = _search_(val, target, index)
      except NotFound as e:
        continue
      else:
        return out

  raise NotFound()


def in_dict(source: dict, target, default = None):
  '''Recursively search a `dict` for a key `target`. If not found, return `default`.'''

  ## TODO implement `index` to find a particular occurrence
  ## TODO? support any dict-like object
  
  try:
    out = _search_(source, target, index = NotImplemented)
  except NotFound:
    return default
  else:
    return out
