
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
import helpers



class DemoAPP(MDApp):
    
    
    def build(self):
        self.theme_cls.primary_palette = "Green"
        scrn = Screen()
        self.entr1 = Builder.load_string(helpers.HelpX)
        btn = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       on_release=self.funct1)
        scrn.add_widget(self.entr1 )
        scrn.add_widget(btn)
        return scrn
        
    def funct1(self,obj):
        print(self.entr1.text)

DemoAPP().run()

