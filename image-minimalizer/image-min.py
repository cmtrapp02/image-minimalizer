import kivy

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button

class ImageMin(App):

    def build(self):
        return self.button_test()

    def button_test(self):
        bttn = Button(text='hello world', font_size=14)

ImageMin().run()