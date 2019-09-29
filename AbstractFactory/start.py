from BrowserView.factory import BrowserFactory
from MobileView.factory import MobileFactory

def create_factory(ui_kind):
  if ui_kind == "mobile":
    return MobileFactory()
  return BrowserFactory()
  
factory = create_factory("mobile")
text = factory.create_text_box("hello factory")
nav = factory.create_navigation_bar(["Item 1", "Item 2"])
print(text.draw_self())
print(text.__class__.__name__)

print(nav.draw_self())
print(nav.__class__.__name__)
print("----------------------------")

factory = create_factory("browser")
text = factory.create_text_box("hello factory")
nav = factory.create_navigation_bar(["Item 1", "Item 2"])
print(text.draw_self())
print(text.__class__.__name__)

print(nav.draw_self())
print(nav.__class__.__name__)
print("----------------------------")
