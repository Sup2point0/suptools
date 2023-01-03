class object:
  def __init__(self, **attributes):
    for attribute in attributes:
      self.__setattr__(attribute, attributes[attribute])
