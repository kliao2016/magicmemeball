import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout

class Controller(BoxLayout):
	def __init__(self):
		super(Controller, self).__init__()

	def buttonClick(self):
		self.lbl.text = "Congratulations!"

class ActionApp(App):
	def build(self):
		return Controller();

class MagicMemeBall(App):

    def build(self):
        return Label(text = "Welcome to Magic Meme Ball! Click start to "
        	+ "to become dank.")

magicMemeBall = ActionApp()
magicMemeBall.run()
