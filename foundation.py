# base classes


class object:
  '''Generic object with any number of attributes.

  ```py
  >>> test = object(x = 6, y = 9)
  >>> print(test)
  object(x = 6, y = 9)
  ```
  '''
  
  def __init__(self, **attributes):
    for attribute in attributes:
      self.__setattr__(attribute, attributes[attribute])

  def __str__(self):
    '''Return a clean string representation of the object’s properties.
    '''
    
    return "object(" + ", ".join(f"{each} = {vars(self)[each]}" for each in vars(self)) + ")"


class series(list):
  '''1-indexed list. Supports all of the functionality of a regular list.
  '''
  
  def __init__(self, /, *args):
    super().__init__([*args])
  
  def __getitem__(self, index):
    if isinstance(index, slice):
      # support for slice indexing (under construction)
      return [super(series, self).__getitem__(i - 1) for i in range(
        index.start or 1,
        index.stop or len(self) + 1,
        abs(index.step) or 1,
      )][::round(index.step / abs(index.step))]
      # reverses list if step is negative, likely faulty
    
    return super(series, self).__getitem__(index - 1)
