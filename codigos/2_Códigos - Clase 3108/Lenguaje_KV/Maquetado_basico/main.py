from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty

class RegistroLayout(BoxLayout):
    clave_match = BooleanProperty(True)
    clave_segura = BooleanProperty(False)

    def registrar(self, usuario, clave1, clave2):
        """

        Machetito para el acceso vía IDs de los widgets
        
        usuario = self.ids.usuario_input.text
        clave1 = self.ids.clave1_input.text
        clave2 = self.ids.clave2_input.text
        
        """
        if clave1 == clave2:
            print(f"Registrando usuario: {usuario} con clave: {clave1}")
            self.clave_match = True
        else:
            print("Las claves no coinciden")
            self.clave_match = False
    
    def verificar_seguridad(self, clave):
        # Verificar seguridad aquí
        seguridad = False
        # Implementa tu lógica para verificar la seguridad de la clave
        if len(clave) >= 8 and any(c.isupper() for c in clave) and any(c.islower() for c in clave) and any(c.isdigit() for c in clave):
            seguridad = True
        self.clave_segura = seguridad

class RegistroApp(App):
    def build(self):
        return RegistroLayout()


if __name__ == '__main__':
    RegistroApp().run()