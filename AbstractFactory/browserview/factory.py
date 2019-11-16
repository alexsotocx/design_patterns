from browserview.text_field import TextField
from browserview.navigation_bar import NavigationBar
from ui_factory import UIFactory


class BrowserFactory(UIFactory):
    def create_text_box(self, text):
        return TextField(text)

    def create_navigation_bar(self, items):
        return NavigationBar(items)
