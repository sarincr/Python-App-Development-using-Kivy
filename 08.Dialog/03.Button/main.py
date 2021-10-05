
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
import helpers


class DemoAPP(MDApp):
    
    
    def build(self):
        self.theme_cls.primary_palette = "Green"
        scrn = Screen()
        self.entr1 = Builder.load_string(helpers.HelpX)
        btn = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       on_press =self.funct1,on_release =self.funct2)
        scrn.add_widget(self.entr1 )
        scrn.add_widget(btn)
        return scrn
        
    def funct1(self,obj):
        print("On Press")
        
    def funct2(self,obj):
        if self.entr1.text is "":
            X = "Please enter a username"
        else:
            X = "Please enter a Password"
        print("Released")
        self.dialog = MDDialog(title='Username check',
                               text=X, size_hint=(0.8, 1),buttons=[MDFlatButton(text='Close', on_release=self.NextFun),
                                        MDFlatButton(text='More')])                               
        self.dialog.open()
    def NextFun(self, obj):
        self.dialog.dismiss()

DemoAPP().run()

