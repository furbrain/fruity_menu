from displayio import Group
from terminalio import FONT
from fruity_menu.abstract import AbstractMenu

from adafruit_display_shapes.rect import Rect
from adafruit_display_text.label import Label

PADDING_V_PX = 1
PADDING_H_PX = 4

class AdjustMenu(AbstractMenu):
    label = ''
    property = None

    def __init__(self, label, height, width):
        self.label = label
        self._width = width
        self._height = height

    def get_display_io_group(self):
        pass

    def get_title_label(self):
        title = Label(FONT, padding_top=PADDING_V_PX, padding_bottom=PADDING_V_PX,padding_right=PADDING_H_PX,padding_left=PADDING_H_PX)
        title.text = self.label
        title.anchor_point = (0.5, 0)
        title.anchored_position = (self._width / 2, 0)
        
        title.color = 0x000000
        title.background_color = 0xffffff
        return title


class BoolMenu(AdjustMenu):
    text_when_true = 'True'
    text_when_false = 'False'

    def __init__(self, property: bool, label, height, width, text_true = 'True', text_false = 'False'):
        self.property = property
        self.text_when_false = text_false
        self.text_when_true = text_true
        super().__init__(label, height, width)

    def get_displayio_group(self):
        grp = Group()
        title_label = self.get_title_label()
        grp.append(title_label)

        prop_text = Label(FONT)
        if (self.property):
            prop_text.text = self.text_when_true
        else:
            prop_text.text = self.text_when_false
        prop_text.anchor_point = (0.5, 0.5)
        prop_text.anchored_position = (self._width / 2, self._height / 2)
        grp.append(prop_text)

        return grp

    def get_value(self):
        return property 

    def click(self):
        return False

    def scroll(self, delta):
        if delta % 2 == 1:
            self.property = not self.property
    
class NumberMenu(AdjustMenu):
    scroll_factor = 1

    def __init__(self, number, label, height, width, scroll_mulitply_factor: int = 1):
        self.property = number
        self.scroll_factor = scroll_mulitply_factor
        super().__init__(label, height, width)

    def get_displayio_group(self):
        grp = Group()
        title_label = self.get_title_label()
        grp.append(title_label)

        prop_text = Label(FONT)
        prop_text.text = str(self.property)
        prop_text.anchor_point = (0.5, 0.5)
        prop_text.anchored_position = (self._width / 2, self._height / 2)
        print(prop_text.anchored_position)
        grp.append(prop_text)
        return grp

    def click(self):
        return False

    def scroll(self, delta):
        self.property = self.property + (self.scroll_factor * delta)
