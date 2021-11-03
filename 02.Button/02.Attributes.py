
from kivy.app import App
from kivy.uix.button import Button


class DemoAPP(App):
        def build(self):
            btn = Button(text ="Click",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(300, 50))
            return btn

demo = DemoAPP()

demo.run()
