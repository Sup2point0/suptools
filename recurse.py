# functions involving recursion


def flatten(iterable) -> list:
  '''Flatten an iterable containing other iterables (except strings) into a list of single values.

  ```py
  >>> l = [1, [2, 3], 4, (5, [6, 7])]
  >>> flatten(l)
  [1, 2, 3, 4, 5, 6, 7]
  ```
  '''
  
  def flattened(content):
    for item in content:
      if hasattr(item, "__iter__") and not isinstance(item, str):
        yield from flattened(item)
      else:
        yield item
  
  return list(flattened(iterable))
