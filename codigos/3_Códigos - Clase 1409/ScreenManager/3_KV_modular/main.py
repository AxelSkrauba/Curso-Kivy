from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from first_screen import FisrtScreen
from second_screen import SecondScreen
from third_screen import ThirdScreen

from kivy.lang import Builder

Builder.load_file('GUI/first_screen.kv')  # Cargar el archivo kv de la pantalla principal
Builder.load_file('GUI/second_screen.kv') # Cargar el archivo kv de la segunda pantalla
Builder.load_file('GUI/third_screen.kv')  # Cargar el archivo kv de la tercera pantalla


class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition(direction='left'))
        sm.add_widget(FisrtScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        return sm

if __name__ == '__main__':
    MyApp().run()
