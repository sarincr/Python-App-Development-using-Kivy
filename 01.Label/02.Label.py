from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles


class DemoAPP(MDApp):
    def build(self):
        lb1 =MDLabel(text="Hello world", halign="center", font_style="Subtitle2")
        return lb1

demo = DemoAPP()
demo.run()


