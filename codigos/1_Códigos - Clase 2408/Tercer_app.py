from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.uix.label import Label

class MiApp(App):

    def build(self):
        layout = BoxLayout(orientation='horizontal')

        btn = Button(text='Presioname') 
        btn.bind(on_press=self.presionado)
        btn.bind(on_release=self.liberado)
        
        self.label = Label(text='Aún no presionado') 
        layout.add_widget(self.label)
        layout.add_widget(btn)

        return layout

    def presionado(self, instance):
        self.label.text = "¡Presionado!"

    def liberado(self, instance):
        self.label.text = "¡Liberado!"
        
if __name__ == '__main__':
    MiApp().run()