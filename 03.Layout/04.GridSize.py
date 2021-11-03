import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        layout.add_widget(Button(text='Hello 1', size_hint_x=None, width=100))
        layout.add_widget(Button(text='World 1'))
        layout.add_widget(Button(text='Hello 2', size_hint_x=None, width=100))
        layout.add_widget(Button(text='World 2'))
        return layout

MyApp().run()
