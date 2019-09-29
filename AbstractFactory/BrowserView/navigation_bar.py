from AbstractNavigationBar import NavigationBar as AbsNavigationBar


class NavigationBar(AbsNavigationBar):
  selected = 0

  def __init__(self, items):
    super().__init__(items)
    self.selected = 0

  def on_click(self, position):
    selected = position
    print("Concrete implementation {items}, selected item {selected}".format(
      items=self.items, selected=self.selected))

