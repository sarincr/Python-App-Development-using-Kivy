
import kivy
 

from kivy.app import App
from kivy.uix.pagelayout import PageLayout
class MainWidget(PageLayout):
    pass
 

class DemoApp(App):
    def build(self):
        return MainWidget()
 
if __name__ == '__main__':
    DemoApp().run()
