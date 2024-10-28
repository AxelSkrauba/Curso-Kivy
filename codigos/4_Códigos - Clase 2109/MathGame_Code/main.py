from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import platform
from kivy.config import Config
from kivy.lang import Builder

from logica.MainScreen import MainScreen
from logica.GameScreen import GameScreen
from logica.ScoreScreen import ScoreScreen

Builder.load_file('GUI/MainScreen.kv')
Builder.load_file('GUI/GameScreen.kv')
Builder.load_file('GUI/ScoreScreen.kv')


class MathGameApp(App):
    # Variables globales a la App
    user_name = ""
    difficulty = ""
    score = ""

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(ScoreScreen(name='score'))
        return sm


if __name__ == '__main__':
    if platform == 'linux':
        # Codigo especifico al ejecutar la App en Linux
        Config.set('graphics', 'width', '400')
        Config.set('graphics', 'height', '900')
    MathGameApp().run()
