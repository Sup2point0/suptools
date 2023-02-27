# functions involving iteration


def bubble(iterable, size: int) -> list:
  '''Iterate through an iterable in a moving 'bubble' of `size`.
  
  ```py
  >>> l = [1, 2, 3, 4, 5, 6, 7]
  >>> bubble(l, 3)
  [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7]]
  ```
  '''
  
  result = []
  i = 0
  while len(iterable) - size >= i:
    result.append(iterable[i:i+size])
    i += 1
  
  return result


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
