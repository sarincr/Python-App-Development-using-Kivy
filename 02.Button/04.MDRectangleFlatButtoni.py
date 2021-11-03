from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

class DemoApp(MDApp):

	def build(self):
		screen = Screen()
		btn= MDRectangleFlatButton(text="Click",pos_hint={'center_x':0.5,'center_y':0.3},on_release=self.funct1)
		screen.add_widget(btn)
		return screen
    
	def funct1(self,obj):
		print("button is pressed!!")
	
if __name__=="__main__":
	DemoApp().run()
