from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
import requests
import json
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget, IconLeftWidget
from kivy.storage.jsonstore import JsonStore

class ProductItem(OneLineAvatarListItem):
    pass

from kivy.lang import Builder

Builder.load_file("search_screen.kv")

class SearchScreen(Screen):
    source = StringProperty()
    store = JsonStore('data.json')      # Ejemplo del JsonStore como DB no relacional

    def search_product(self, search_term):
        print("Init search")
        try:
            api_url = f"https://api.mercadolibre.com/sites/MLA/search?q={search_term}&limit=20&offset=1"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = json.loads(response.text)
            
                results_list = self.ids.results_list
                results_list.clear_widgets()  # Limpiar la lista antes de agregar nuevos elementos

                for item in data['results']:
                    product_name = item.get('title', 'Sin nombre')
                    product_price = item.get('price', 0)
                    product_image_url = item.get('thumbnail', '')
                    
                    # Crear un elemento MD para mostrar el producto
                    product_item = ProductItem(text=f"{product_name} - Precio: ${product_price}")
                    
                    # Agregar una imagen a la izquierda del elemento MD (si hay una URL de imagen)
                    if product_image_url:
                        product_item.add_widget(ImageLeftWidget(source=product_image_url))
                    else:
                        product_item.add_widget(IconLeftWidget(icon="alert-circle"))
                    
                    # Agregar el elemento a la lista
                    results_list.add_widget(product_item)
                
                self.ids.results_label.text = "Datos Procesados"

            else:
                self.ids.results_label.text = "Error al obtener resultados de la API."
        except Exception as e:
            self.ids.results_label.text = f"Error: {str(e)}"
            print(f"Error: {str(e)}")

        self.store.put('data', value=data)
        print("Stop search")