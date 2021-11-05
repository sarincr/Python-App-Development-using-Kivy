from kivy.app import App
from kivy.uix.switch import Switch

 
class SwitchApp(App):
  def build(self):
 
    switch = Switch()
 
    switch.bind(active=self.switch_state)
    return switch
 
  def switch_state(self, instance, value):
      print('Switch is', value)
 
SwitchApp().run()
