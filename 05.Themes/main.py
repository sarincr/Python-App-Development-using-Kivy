from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Red"
		return Builder.load_file('color_theme.kv')

		

MainApp().run()
