from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Salom, bu mening birinchi APK ilovam!")

if __name__ == "__main__":
    MyApp().run()