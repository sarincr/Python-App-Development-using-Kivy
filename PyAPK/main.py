 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class MyApp(App):
    def build(self):
        self.layout = BoxLayout()
        self.btn = Button(text="press", on_press=self.my_btn_method)
        self.lbl = Label(text="")
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.lbl)

        return self.layout

    def my_btn_method(self, instance):
        self.lbl.text = str(random.randint(0,100))

MyApp().run()
