from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore
from kivy.lang import Builder

Builder.load_file("interfaz.kv")

class FileManagerApp(MDApp):
    def build(self):
        self.store = JsonStore('data.json')
        return FileManagerScreen()

    def save_data(self, data):
        self.store.put('data', value=data)
        print("Datos guardados:", data)

    def load_data(self):
        try:
            data = self.store.get('data')
        except KeyError:
            return None
        return data['value'] if data else None

class FileManagerScreen(Screen):
    pass

if __name__ == "__main__":
    FileManagerApp().run()