from kivy.uix.screenmanager import Screen


class FisrtScreen(Screen):
    def switch_to_second(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'
