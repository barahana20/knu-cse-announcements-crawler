from typing import Callable

class Observer:
  def __init__(self, value, callback:Callable):
    self.__value = value
    self.__callback = callback
  
  @property
  def value(self):
    print('Someone has read the value:', self.__value)
    return self.__value
  
  @value.setter
  def value(self, new_value):
    self.__callback(new_value)
    self.__value = new_value

ob = Observer('강아지', lambda s: print('write the value!:', s))
ob.value

ob.value = '고양이'
