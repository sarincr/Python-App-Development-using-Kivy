
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
                   pos =(300, 250))
            btn.bind(on_press = self.funct1)
            return btn
        def funct1(self, event):
            print("Button pressed")

demo = DemoAPP()

demo.run()
