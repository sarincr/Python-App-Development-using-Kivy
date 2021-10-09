
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):

    def build(self):
        scrn = Screen()
        scrl = ScrollView()

        lst= MDList()
        items = ThreeLineListItem(text= "Item 1",   secondary_text='Item 2', tertiary_text='Item 3')
        lst.add_widget(items)
        scrl.add_widget(lst)
        scrn.add_widget(scrl)
        return scrn


DemoApp().run()