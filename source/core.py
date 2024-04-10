'''
Implements fundamental utility functions and classes.
'''


def init(obj, **attributes):
  '''Initialise an object with the given attributes.'''

  Object.__init__(obj, **attributes)


class Object:
  '''Generic object with any attributes.'''
  
  def __init__(self, **attributes):
    '''Create a generic object with any given attributes.'''
    
    for attribute in attributes:
      self.__setattr__(attribute, attributes[attribute])

  def __str__(self):
    '''Return a clean string representation of the object’s properties.'''
    
    return "object(" + ", ".join(f"{each} = {vars(self)[each]}" for each in vars(self)) + ")"
