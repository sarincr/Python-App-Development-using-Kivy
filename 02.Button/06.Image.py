import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics', 'resizable', True)   

class Button_Demo(App):
    def build(self):
        btn = Button(color =(1, 0, .65, 1),  background_normal = '3.jpg', size_hint = (.4, .4), pos_hint = {"x":0.39, "y":0.3}   )    
        return btn

root = Button_Demo()    
root.run()  
