import kivy
from kivy.app import App

from kivy.uix.label import Label

class MyLabelApp(App):
        def build(self):
		lbl = Label(text ="This is a txt label")
		return lbl

label = MyLabelApp()

label.run()
