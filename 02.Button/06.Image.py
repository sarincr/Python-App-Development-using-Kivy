import kivy

from kivy.app import App
from kivy.uix.button import Button


class Button_Demo(App):
    def build(self):
        btn = Button( background_normal = '3.jpg', size_hint = (.1, .1), pos_hint = {"x":0.39, "y":0.3}   )    
        return btn

root = Button_Demo()    
root.run()  
