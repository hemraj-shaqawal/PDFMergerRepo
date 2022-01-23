from email.mime import multipart
from re import MULTILINE
import kivy
kivy.require('1.10.0')
  
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from Merger.PDFMErger import PdfMerger
import  logging as logger

logger.basicConfig(filename="appLog.log",level= logger.INFO,format="%(asctime)s %(levelname)s %(message)s")

# Inherit Kivy's App class which represents the window
# for our widgets
# HelloKivy inherits all the fields and methods
# from Kivy

class MyGridLayout(GridLayout):

        def __init__(self, **kwargs):
            super(MyGridLayout, self).__init__(**kwargs)

            # set column
            self.cols = 2

            self.name = TextInput(multiline=False)
            self.add_widget(self.name)

            self.btn = Button(text="Submit",
                    font_size="20sp",
                    background_color=(1, 1, 1, 1),
                    color=(1, 1, 1, 1),
                    size=(32, 32),
                    size_hint=(.2, .2),
                    pos=(300, 250))

            self.add_widget(self.btn)

            # bind() use to bind the button to function callback
            self.btn.bind(on_press=self.callback)
            

        def callback(self,event):
            try:
                print("button pressed",self.name.text)
                obj = PdfMerger(self.name.text)
            except Exception as e:
                logger.exception("Error Occured ===>"+str(e))

class PDFMergerApp(App):
    
    # This returns the content we want in the window
    def build(self):
        return MyGridLayout()



if __name__ == '__main__':
    PDFMergerApp().run()