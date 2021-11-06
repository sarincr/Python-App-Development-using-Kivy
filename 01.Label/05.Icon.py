
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles


class DemoApp(MDApp):
    def build(self):
        label = MDIcon(icon="language-python", halign="center")
        return label


DemoApp().run()