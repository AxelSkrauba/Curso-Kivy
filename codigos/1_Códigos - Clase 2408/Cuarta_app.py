from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput  
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox

class MiApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.pwd1 = TextInput(password=True)
        layout.add_widget(self.pwd1)

        self.pwd2 = TextInput(password=True) 
        layout.add_widget(self.pwd2)

        self.chk = CheckBox()
        self.chk.bind(active=self.on_checkbox_active)
        layout.add_widget(self.chk)

        btn = Button(text='Verificar', on_press=self.verificar)
        layout.add_widget(btn)

        return layout

    def verificar(self, instance):
        if self.pwd1.text == self.pwd2.text:
            print("Las contraseñas coinciden")
        else:
            print("Las contraseñas no coinciden")
    
    def on_checkbox_active(self, checkbox, value):
        if value:
            self.pwd1.password = False
            self.pwd2.password = False
        else:
            self.pwd1.password = True
            self.pwd2.password = True

if __name__ == '__main__':
    MiApp().run()