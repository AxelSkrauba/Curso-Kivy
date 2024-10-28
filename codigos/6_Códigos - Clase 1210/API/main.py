from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from search_screen import SearchScreen  # Importa la pantalla de búsqueda desde search_screen.py

class PriceTrackerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        
        # Crea un administrador de pantallas (ScreenManager)
        self.screen_manager = ScreenManager()
        
        # Agrega la pantalla de búsqueda al administrador de pantallas
        search_screen = SearchScreen(name="search_screen")
        self.screen_manager.add_widget(search_screen)
        
        return self.screen_manager

if __name__ == "__main__":
    PriceTrackerApp().run()