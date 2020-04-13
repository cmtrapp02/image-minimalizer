import kivy

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang.builder import Builder


class ImageMin(App):

    def build(self):
        return self.button_test()

    def button_test(self):
        return Button(text='[size=10]Hello World[/size]', markup=True)

    def text_test(self):
        return Label(text='hello world!', font_size=50)

ImageMin().run()