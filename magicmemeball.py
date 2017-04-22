import kivy
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
kivy.require('1.9.1')

Builder.load_string("""
<StartLayout>:
    orientation: 'vertical'

    BoxLayout:
    	center: 0.5, 0.5
    	size: self.parent.size
		pos: self.parent.pos

	    Button:
	        text: 'Click to find your spirit meme!'
	        Image:
	            source: 'images/magic8ball.png'
	            size_hint: 0.5, 0.5
	            anchor_x: 'center'
	            anchor_y: 'center'
	            size: 300, 300
	            allow_stretch: True
	            keep_ratio: True
""")

class ActionApp(App, BoxLayout):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		return StartLayout()

class StartLayout(BoxLayout):
	def build(self):
		return self

magicMemeBall = ActionApp()
magicMemeBall.run()
