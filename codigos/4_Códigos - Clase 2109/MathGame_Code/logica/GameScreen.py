from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import StringProperty
import random


class CustomButton(Button):
    pass


class GameScreen(Screen):
    name_label = StringProperty()
    timer_label = StringProperty()
    expression_label = StringProperty()

    def on_enter(self):
        # Esta funcion se ejecuta al entrar la pantalla en escena

        self.name_label = "Nombre: " + App.get_running_app().user_name
        self.time_left = 30     # Variable para la cuenta regresiva del timer, en segundos
        self.score = 0          # Variable para almacenar el conteo de puntos

        self.buttons_box = self.ids.button_list  # Box para contener botones dinamicos
        self.buttons = []                        # Lista para acceder a los botones disponibles
        
        # Codigo para la logica del juego segun dificultar
        difficulty = App.get_running_app().difficulty
        self.operands = list(range(1, 11)) if difficulty == 'Facil' else list(range(1, 101))
        self.operations = ['+', '-', '*', '/'] if difficulty == 'Dificil' else ['+', '-']

        self.set_buttons()  # Construye botones
        self.game_cycle()   # Construye una propuesta de ecuacion
        self.start_timer()  # Inicia el timer

    def game_cycle(self):
        operand1 = random.choice(self.operands)
        operand2 = random.choice(self.operands)
        operation = random.choice(self.operations)
        self.expression_label = f"{operand1} {operation} {operand2}"
        self.correct_answer = str(eval(self.expression_label))
        self.update_buttons()

    def set_buttons(self):
        button_layout = BoxLayout(orientation='vertical', spacing=10)
        for _ in range(2):
            row_layout = BoxLayout(spacing=10)
            for _ in range(2):
                button = CustomButton()
                button.bind(on_press=self.check_answer)
                self.buttons.append(button)
                row_layout.add_widget(button)
            button_layout.add_widget(row_layout)
        self.buttons_box.clear_widgets()
        self.buttons_box.add_widget(button_layout)

    def update_buttons(self):
        # Actualiza el texto de los botones segun la nueva ecuacion

        # El valor correcto se asegura en uno de los botones existentes
        correct_button = random.choice(self.buttons)
        correct_button.text = self.correct_answer

        # Los demas botones contienen un valor aleatorio
        for button in self.buttons:
            if button != correct_button:
                # Mejorar el rango y tipo segun nivel
                # Por ejemplo, si el operador es division... habra un solo boton con valor flotante
                button.text = str(random.randint(0, 200))

    def check_answer(self, instance):
        # Se verifica si el boton presionado contiene la respuesta correcta
        if instance.text == self.correct_answer:
            print("Acierto!")
            self.score += 1
            self.time_left += 2     # Ejemplo de feedback, bonificacion de tiempo
            print(self.score)
        else:
            self.time_left -= 7     # Ejemplo de feedback, penalizacion de tiempo
            print("Error!")
        self.game_cycle()           # Generacion de nueva ecuacion

    def start_timer(self):
        self.evento_reloj = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        # Se llama cada segundo 
        self.time_left -= 1
        if self.time_left <= 0:
            print("Temino el tiempo")
            self.evento_reloj.cancel()
            App.get_running_app().score = str(self.score)
            self.manager.current = 'score'
        else:
            self.timer_label = '{:02d}:{:02d}'.format(*divmod(self.time_left, 60))
