from browserview.factory import BrowserFactory
from mobileview.factory import MobileFactory

def create_factory(ui_kind):
  if ui_kind == "mobile":
    return MobileFactory()
  return BrowserFactory()
  
def run(factory):
  text = factory.create_text_box("hello factory")
  nav = factory.create_navigation_bar(["Item 1", "Item 2"])
  text.on_click()
  print(text.draw_self())
  print(text.__class__.__name__)
  
  print(nav.draw_self())
  print(nav.__class__.__name__)
  print("----------------------------")  
  

run(create_factory("mobile"))
run(create_factory("browser"))
