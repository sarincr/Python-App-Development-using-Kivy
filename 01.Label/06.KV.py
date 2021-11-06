from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
Screen:

    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "MDLabel1"

        MDLabel:
            text: "MDLabel2"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()
