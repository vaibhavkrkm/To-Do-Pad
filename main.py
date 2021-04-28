from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.utils import rgba
import os


class MainLayout(Widget):
	text_input = ObjectProperty(None)       # this is the text input I need to access
	theme_button = ObjectProperty(None)
	clear_button = ObjectProperty(None)

	selected_theme = "dark"

	def on_theme_button_pressed(self):
		if(self.selected_theme == "dark"):
			# changing the theme variable
			self.selected_theme = "light"

			# changing the text color variable
			self.text_color = rgba(0, 0, 0)

			# changing colors for text input
			self.text_input.background_color = rgba(255, 255, 255)
			self.text_input.foreground_color = self.text_color

			# changing colors for theme button
			self.theme_button.background_color = rgba(64, 170, 64)
			self.theme_button.color = rgba(0, 0, 0)
		else:
			# changing the theme variable
			self.selected_theme = "dark"
			
			# changing the text color variable
			self.text_color = rgba(255, 255, 255)

			# changing colors for text input
			self.text_input.background_color = rgba(0, 0, 0)
			self.text_input.foreground_color = self.text_color

			# changing colors for theme button
			self.theme_button.background_color = rgba(46, 46, 127)
			self.theme_button.color = rgba(255, 255, 255)

	def on_clear_button_pressed(self):
		self.text_input.text = ""


class ToDoPadApp(App):
	def build(self):
		return MainLayout()

	def on_start(self):
		self.load_data()

	def on_stop(self):
		self.save_data(self.root.text_input.text)

	def load_data(self):
		if(os.path.isfile("save.data")):
			with open("save.data", "r") as f:
				self.root.text_input.text = f.read()

	def save_data(self, data):
		# saves the data into a file
		with open("save.data", "w") as f:
			f.write(data)


if __name__ == '__main__':
	ToDoPadApp().run()
