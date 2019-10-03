class AbstractNavigationBar:
  def __init__(self, items):
    self.items = items

  def on_click(self, position):
    print("Hello World")
  
  def draw_self(self):
    raise NotImplementedError()

