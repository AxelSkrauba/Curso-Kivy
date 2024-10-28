from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


class CustomLabel(Label):
    pass


class ScoreScreen(Screen):
    def on_enter(self):
        self.score_list_layout = self.ids.score_list
        new_puntaje = CustomLabel(text='{} ({}): {}'.format(
            App.get_running_app().user_name,
            App.get_running_app().difficulty,
            App.get_running_app().score,
        ))
        self.score_list_layout.add_widget(new_puntaje)
