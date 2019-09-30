from abstract_navigation_bar import AbstractNavigationBar


class MobileNavigationBar(AbstractNavigationBar):
  selected = 0

  def __init__(self, items):
    super().__init__(items)
    self.selected = 0

  def __ontap(self, position):
    self.selected = position
    print("Do on tap at {position}".format(position=position))

  def on_click(self, position):
    self.__onTap(position)

  def draw_self(self):
    return "Drawing mobile Navigation Bar {items}, selected item {selected}".format(
      items=self.items, selected=self.selected)

