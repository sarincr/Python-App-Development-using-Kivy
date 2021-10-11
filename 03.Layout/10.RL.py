
from kivy.app import App

from kivy.uix.relativelayout import RelativeLayout
  
from kivy.uix.button import Button
from kivy.config import Config 

Config.set('graphics', 'resizable', True) 

class DemoAPP(App):
        def build(self):
            lay1 =  RelativeLayout() 
            bt1 = Button(text ="Click",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(300, 250))
            lay1.add_widget(bt1)
            return lay1


demo = DemoAPP()
demo.run()
