from abstract_navigation_bar import AbstractNavigationBar


class NavigationBar(AbstractNavigationBar):
    def __init__(self, items):
        super().__init__(items)
        self.selected = 0

    def on_click(self, position):
        selected = position
        print("Concrete implementation {items}, selected item {selected}".format(
            items=self.items, selected=self.selected))

    def draw_self(self):
        return "Drawing Browser Navigation Bar {items}, selected item {selected}".format(
            items=self.items, selected=self.selected)
