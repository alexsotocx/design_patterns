from abstract_textview import AbstractTextview


class TextField(AbstractTextview):
    def __init__(self, text):
        super().__init__(text)
        self.focus = False

    def on_click(self):
        print("Focus!")
        self.focus = True
        print(self.text)

    def draw_self(self):
        return "Text: {text} is focused = {focused}".format(text=self.text, focused=self.focus)
