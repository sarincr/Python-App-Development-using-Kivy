from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDRaisedButton:
    text: "MDRAISEDBUTTON"
    md_bg_color: 1, 0, 1, 1
'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()
