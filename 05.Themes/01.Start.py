

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton


class DemoAPP(MDApp):
    
    
    def build(self):
        scrn = Screen()
        btnflt = MDFlatButton(text="Hello Button", pos_hint={'center_x' : 0.5, 'center_y' : 0.5})
        scrn.add_widget(btnflt)
        return scrn
        



demo = DemoAPP()
demo.run()
