import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('searchBar.kv')
Builder.load_file('searchbarLabel.kv')


class GuestSearchApp(App):
    pass


GuestSearchApp().run()
