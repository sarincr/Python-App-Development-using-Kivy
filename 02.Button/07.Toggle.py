from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
 
 
class SimpleApp(App):
    def build(self):
 
        b = ToggleButton(text="Click")
        return b
 
 
if __name__ == "__main__":
    SimpleApp().run()
