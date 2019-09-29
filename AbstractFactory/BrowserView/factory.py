from BrowserView.text_field import TextField
from BrowserView.navigation_bar import NavigationBar
from UI_factory import UIFactory

class BrowserFactory(UIFactory):
  def create_text_box(self, text):
    return TextField(text)
  
  def create_navigation_bar(self, items):
    return NavigationBar(items)
  
