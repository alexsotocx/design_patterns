from mobile_view.text_field import TextInput
from mobile_view.navigation_bar import MobileNavigationBar
from ui_factory import UIFactory

class MobileFactory(UIFactory):
  def create_text_box(self, text):
    return TextInput(text)
  
  def create_navigation_bar(self, items):
    return MobileNavigationBar(items)
  
