from AbstractTextView import TextView

class TextField(TextView):
  focus = False
  
  def __init__(self, text):
    super().__init__(text)
    
  def on_click(self):
    print("here it did click")
    self.focus = True
    print(self.text)
    
  def draw_self(self):
    return "Text: {text} is focused = {focused}".format(text=self.text, focused=self.focus)
