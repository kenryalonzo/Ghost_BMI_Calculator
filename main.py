from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty

from screen_manager import MyScreenManager

class ScreenBrowser(MyScreenManager):
    pass

class MainApp(App):
    manage = ObjectProperty()
    def build(self):
        self.manage = ScreenBrowser()
        return self.manage
    pass


app = MainApp()
app.run()