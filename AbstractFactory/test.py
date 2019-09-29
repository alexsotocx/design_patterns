from BrowserView.factory import BrowserFactory

factory = BrowserFactory()
text = factory.create_text_box("text field")
print(text.draw_self())
