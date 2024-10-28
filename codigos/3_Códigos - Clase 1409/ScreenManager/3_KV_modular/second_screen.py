from kivy.uix.screenmanager import Screen


class SecondScreen(Screen):
    def switch_to_third(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'third'
