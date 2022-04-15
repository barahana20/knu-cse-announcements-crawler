from typing import Optional, Sequence
from click import DateTime

class IntOrDateTime(DateTime):
  name='int or datetime'
  
  def __init__(self, formats: Optional[Sequence[str]] = None):
      super().__init__(formats)

  def convert(self, value, param, ctx):
    if value is None:
      return None
    
    try:
      return int(value)
    except:
      return self.convert(value)

    
    
  

      
