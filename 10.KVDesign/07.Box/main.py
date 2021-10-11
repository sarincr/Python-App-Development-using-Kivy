
import kivy
 

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainWidget(BoxLayout):
    pass
 

class DemoApp(App):
    def build(self):
        return MainWidget()
 
if __name__ == '__main__':
    DemoApp().run()
