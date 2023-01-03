class object:
  '''Generic object with any number of attributes.'''
  
  def __init__(self, **attributes):
    for attribute in attributes:
      self.__setattr__(attribute, attributes[attribute])


class series(list):
  '''1-indexed list.'''
  
  def __init__(self, /, *args):
    super().__init__([*args])
  
  def __getitem__(self, index):
     return super().__getitem__(index - 1)
