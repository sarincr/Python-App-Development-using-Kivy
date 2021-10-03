
from kivy.app import App
from kivy.uix.button import Button


class DemoAPP(App):
        def build(self):
            bt1 = Button(text ="Click Here")
            return bt1

demo = DemoAPP()
demo.run()
