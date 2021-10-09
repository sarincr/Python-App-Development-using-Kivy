from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList 
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView



class DemoApp(MDApp):

    def build(self):
        scrn = Screen()

        scrl =ScrollView()

        lst = MDList()
        for i in range(20):

            items = OneLineIconListItem(text=str(i) + ' item')
            lst.add_widget(items)

        scrl.add_widget(lst)

        scrn.add_widget(scrl)
        return scrn


DemoApp().run()