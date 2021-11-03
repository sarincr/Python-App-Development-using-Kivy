from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles


class DemoAPP(MDApp):
    def build(self):
        label = MDLabel(text="Hello world", halign="center", theme_text_color="Primary",font_style="Subtitle2")
        return label


DemoAPP().run()
