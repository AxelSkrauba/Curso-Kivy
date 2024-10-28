from kivy.uix.screenmanager import Screen


class ThirdScreen(Screen):
    def switch_to_main(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'
