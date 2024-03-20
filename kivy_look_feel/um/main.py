from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        button = Button(text='Click Me?', size_hint=(None, None), size=(200, 50), pos=(100, 100),
                        background_color=(0, 1, 0, 1), color=(1, 1, 1, 1), font_size=20)
        return button


if __name__ == "__main__":
    MyApp().run()
