

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder


X = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""

class DemoAPP(MDApp):
    
    
    def build(self):
        scrn = Screen()
        entr1 = Builder.load_string(X)
        scrn.add_widget(entr1)
        return scrn
        


DemoAPP().run()

