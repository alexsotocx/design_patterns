class AbstractTextview:
  text = ''
  
  def __init__(self, text):
    self.text = text
    
  def on_click(self):
    raise NotImplementedError()
    
  def draw_self(self):
    raise NotImplementedError()
