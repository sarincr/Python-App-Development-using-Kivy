from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDRoundFlatIconButton:
    icon: "android"
    text: "MDROUNDFLATICONBUTTON"

'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()
