from kivy.app import App
from kivy.uix.textinput import TextInput
 
 
class SimpleApp(App):
    def build(self):
        t = TextInput(font_size=150)
        return t
 
 
if __name__ == "__main__":
    SimpleApp().run()
