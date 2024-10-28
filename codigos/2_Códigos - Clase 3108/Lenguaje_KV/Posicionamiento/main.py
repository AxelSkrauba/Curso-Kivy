from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class EjemploLayout(FloatLayout):
    pass
    
class PosicionamientoApp(App):
    def build(self):
        return EjemploLayout()


if __name__ == '__main__':
    PosicionamientoApp().run()