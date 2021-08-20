import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
Builder.load_file('searchBar.kv')



class GuestSearchApp(App):
    pass


GuestSearchApp().run()
