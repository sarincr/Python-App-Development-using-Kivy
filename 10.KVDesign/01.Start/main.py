 
import kivy
from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.widget import Widget


class MyGrid(Widget):
    pass


class MyApp(App): 
    def build(self):
        return MyGrid()


MyApp().run()
