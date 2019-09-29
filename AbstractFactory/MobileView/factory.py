from MobileView.text_field import TextInput
from MobileView.navigation_bar import MobileNavigationBar
from UI_factory import UIFactory

class MobileFactory(UIFactory):
  def create_text_box(self, text):
    return TextInput(text)
  
  def create_navigation_bar(self, items):
    return MobileNavigationBar(items)
  
