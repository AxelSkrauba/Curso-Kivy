from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import threading


class Pantalla(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num = 0

        # Tarea para otro hilo
        t = threading.Thread(target=self.otro_hilo) # Probar de cerrar la aplicacion mientra corre el hilo
        '''
        Subproceso (Thread): Un subproceso es una unidad de ejecución independiente en un programa. 
        Puedes crear múltiples subprocesos que se ejecutan concurrentemente.

        Funciones Concurrentes: Puedes asignar funciones para ejecutarse en subprocesos separados, 
        lo que permite realizar múltiples tareas de manera concurrente.

        Los subprocesos pueden recibir argumentos de funciones para realizar tareas específicas.

        # Crear un subproceso con argumentos
        thread = threading.Thread(target=worker_function, args=("Hola", "Mundo"))
        '''

        #t = threading.Thread(target=self.otro_hilo, daemon=True) # Probar ahora de cerrar la aplicacion mientra corre el hilo
        '''
        Un daemon es un subproceso que se ejecuta en segundo plano y se detiene cuando 
        la aplicación principal se cierra. Los subprocesos regulares esperan a que terminen antes 
        de que la aplicación principal se cierre.
        '''
        
        # Inicia el hilo
        t.start()
    
    def otro_hilo(self):
        for i in range(500000):
            # Tarea demandante
            # Congelaria la carga de la interfaz en el hilo principal
            print(i)

    def count(self):
        self.num += 1
        self.ids.label.text = str(self.num)

class MainApp(App):
    def build(self):
        return Pantalla()

MainApp().run()