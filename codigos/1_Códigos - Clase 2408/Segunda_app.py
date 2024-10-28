from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MiApp(App):

    def build(self):
        self.title = "Mi Aplicación"
        b = BoxLayout(orientation='vertical')
        
        self.txt_input = TextInput(multiline=False)
        b.add_widget(self.txt_input)

        btn = Button(text="Saludar",
                     on_press=self.saludar) 
        b.add_widget(btn)

        return b

    def saludar(self, obj):
        nombre = self.txt_input.text
        print("¡Hola {}!".format(nombre))
        self.txt_input.text = ""

if __name__ == "__main__":
    MiApp().run()