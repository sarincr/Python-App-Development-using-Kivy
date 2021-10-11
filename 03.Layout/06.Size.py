
import kivy

from kivy.app import App

from kivy.uix.button import Button
 

from kivy.uix.gridlayout import GridLayout

class Grid_LayoutApp(App):
 

    def build(self):

        layout = GridLayout(cols = 2)
 

        layout.add_widget(Button(text ='Element A  1', size_hint_x = None, width = 100))
        layout.add_widget(Button(text ='Element B 1'))

        layout.add_widget(Button(text ='Element A  2'))
        layout.add_widget(Button(text ='Element B 2'))

        layout.add_widget(Button(text ='Element A  3', size_hint_x = None, width = 100))
        layout.add_widget(Button(text ='Element B 3'))
 

        layout.add_widget(Button(text ='Element A  4'))
        layout.add_widget(Button(text ='Element B 4'))
 

        return layout
 

root = Grid_LayoutApp()

root.run()