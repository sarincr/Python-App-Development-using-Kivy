

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
import helpers



class DemoAPP(MDApp):
    
    
    def build(self):
        scrn = Screen()
        entr1 = Builder.load_string(helpers.HelpX)
        scrn.add_widget(entr1)
        return scrn
        


DemoAPP().run()

