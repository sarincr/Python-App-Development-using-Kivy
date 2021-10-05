

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField

class DemoAPP(MDApp):
    
    
    def build(self):
        scrn = Screen()
        entr1 = MDTextField(text="Enter Name : ", pos_hint={'center_x' : 0.5, 'center_y' : 0.5}, size_hint=(0.5,1))
        scrn.add_widget(entr1)
        return scrn
        


DemoAPP().run()

