from AbstractTextView import TextView

class TextInput(TextView):
  focus = False
  
  def __init__(self, text):
    super().__init__(text)
    
  def on_click(self):
    print("on tap")
    self.focus = True
    
  def draw_self(self):
    return "Mobile Text: {text} is focused = {focused}".format(text=self.text, focused=self.focus)
