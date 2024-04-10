'''
Functions involving iteration and iterables.
'''

from typing import Iterable
from collections.abc import Generator


def bubble(seq: Iterable, /, size: int = 2) -> Generator:
  '''Return an iterator for traversing an iterable in a moving ‘bubble’ of `size`.
  
  ```py
  >>> l = list(range(7))
  >>> for each in bubble(l, 3):
        print(each)
  (1, 2, 3)
  (2, 3, 4)
  (3, 4, 5)
  (4, 5, 6)
  ```
  '''

  if not isinstance(seq, Iterable):
    raise TypeError(f"sequence must be an iterable, not {type(seq)}")
  if not isinstance(size, int):
    raise TypeError(f"size must be an int, not {type(seq)}")
  if size < 1:
    raise ValueError("size must be positive")

  idx = 0
  apex = len(seq) - size

  while idx < apex:
    yield tuple(seq[i] for i in range(idx, idx + size))
    idx += 1

  raise GeneratorExit()


def has(iterable, *values, every = False) -> bool:
  '''Check if `iterable` contains any of `values`.
  
  If `every` is `True`, it must contain every specified value.

  ```py
  >>> l = ['sup', 'nova', 'shard']
  >>> has(l, 'soup')
  False
  >>> has(l, 'sup')
  True
  >>> has(l, 'sup', 'shard')
  True
  >>> has(l, 'sup', 'soup')
  True
  >>> has(l, 'sup', 'soup', every = True)
  False
  ```
  '''

  out = (each in iterable for each in values)
  return all(out) if every else any(out)


def index_any(iterable, *values, check = False) -> int | tuple[int, any] | None:
  '''Find index of first occurence of any value within `values`.

  If `check` is True, a tuple containing which value was found is returned instead.
  
  Returns `None` if no occurrences are found.
  '''

  for i, each in enumerate(iterable):
    if each in values:
      if check:
        for value in values:
          if value == each:
            return (i, value)
      else:
        return i
  
  return None


def indices(source, content) -> list[int]:
  '''Find indices of all occurences of `content` in an iterable.
  
  ```py
  >>> l = ['sup', 'nova', 'sup', 'shard', 'nova', 'sup']
  >>> indices(l, 'sup')
  [0, 2, 5]
  >>> indices(l, 'nova')
  [1, 4]
  ```
  '''
  
  result = []
  
  for i, each in enumerate(source):
    if each == content:
      result.append(i)
  
  return result
