from mobileview.text_field import TextInput
from mobileview.navigation_bar import MobileNavigationBar
from ui_factory import UIFactory


class MobileFactory(UIFactory):
    def create_text_box(self, text):
        return TextInput(text)

    def create_navigation_bar(self, items):
        return MobileNavigationBar(items)
