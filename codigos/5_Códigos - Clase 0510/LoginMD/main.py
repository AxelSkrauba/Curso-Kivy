from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty

Builder.load_file("login.kv")


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class LoginScreen(Screen):
    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text

        # Aquí puedes agregar la lógica de autenticación
        if username == "usuario" and password == "contraseña":
            # Autenticación exitosa
            self.ids.info_label.text = "Inicio de sesión exitoso"
        else:
            # Autenticación fallida
            self.ids.info_label.text = "Inicio de sesión fallido"


class MyApp(MDApp):
    def build(self):
        # Personalización de tema y estilo
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return LoginScreen()


MyApp().run()
