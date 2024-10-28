from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, CardTransition
from kivy.uix.button import Button


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.add_widget(Button(text="Ir a la Segunda Pantalla",
                        on_release=self.switch_to_second))

    def switch_to_second(self, instance):
        # De esta forma si hace falta el 2do argumento, no lo usamos nada más.
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'second'


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.add_widget(Button(text="Ir a la Tercera Pantalla",
                        on_release=self.switch_to_third))

    def switch_to_third(self, instance):
        self.manager.transition = CardTransition(direction='left')
        self.manager.current = 'third'


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super(ThirdScreen, self).__init__(**kwargs)
        self.add_widget(
            Button(text="Regresar a la Pantalla Principal", on_release=self.switch_to_main))

    def switch_to_main(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'main'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        return sm


if __name__ == '__main__':
    MyApp().run()
