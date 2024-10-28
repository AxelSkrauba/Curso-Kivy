from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Pantalla(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num = 0
        for i in range(500000):
            # Tarea demandante
            # Congelaria la carga de la interfaz
            print(i)
    
    def count(self):
        self.num += 1
        self.ids.label.text = str(self.num)

class MainApp(App):
    def build(self):
        return Pantalla()

MainApp().run()