
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class GridLayout_demo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        self.rows=2
        self.cols=1
        self.lb1 = Label(text ="Label is Added on screen !!:):)")
        self.add_widget(self.lb1)
        self.btn = Button(text ="Click",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(62, 62),
                   size_hint =(.6, .6),
                   pos =(300, 250))
        self.add_widget(self.btn)

class DemoAPP(App):
        def build(self):
            return GridLayout_demo()


demo = DemoAPP()
demo.run()
