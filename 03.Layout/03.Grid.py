import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Grid_LayoutApp(App):

	def build(self):
		layout = GridLayout(cols = 2)
		layout.add_widget(Button(text ='Hello 1'))
		layout.add_widget(Button(text ='World 1'))
		return layout



Grid_LayoutApp().run()
