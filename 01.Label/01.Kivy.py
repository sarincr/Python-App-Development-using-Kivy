import kivy



from kivy.app import App


from kivy.uix.label import Label



class DemoAPP(App):
    def build(self):
        lb1 = Label(text ="Label is Added on screen !!:):)")
        return lb1

demo = DemoAPP()
demo.run()


