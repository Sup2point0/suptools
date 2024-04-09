'''
Functions involving recursion.
'''


def locate(source, content):
  '''Check if a multi-level iterable contains an item.
  '''
  
  def recurse(source, target):
    for each in source:
      if each == target:
        return True
      elif hasattr(each, '__iter__') and not isinstance(each, str):
        return recurse(each, target)
    return False
  
  return recurse(source, content)


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


def attain(source, *, depth = True) -> list:
  '''Obtain all objects in the entire directory tree of an object, such as a class or module.

  By default the value of the object is output; if `depth` is `False` the name will be output instead.

  ```py
  >>> class Test:
        sup = 2.0

        class Tools:
          nova = 4.2
          shard = 6.9
  
  >>> [i for i in attain(Test)]
  [2.0, 4.2, 6.9]
  >>> [i for i in attain(Test, depth = False)]
  ['nova', 'shard', 'sup']
  ```
  '''
  
  for item in [i for i in dir(source) if not i.startswith("__")]:
    if not isclass(getattr(source, item)):
      yield getattr(source, item) if depth else item
    else:
      yield from attain(getattr(source, item), depth = depth)


def collapse_dict(source: dict, levels: int = None) -> dict:
 '''Collapse a `dict` or similar mapping such that'''
