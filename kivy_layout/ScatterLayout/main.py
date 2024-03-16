from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button


class ScatterLayoutApp(App):
    def build(self):
        layout = ScatterLayout()

        button = Button(text="Scalable, Rotable, and Movable", size_hint=(None, None), size=(200, 100))

        layout.add_widget(button)

        return layout


if __name__ == '__main__':
    ScatterLayoutApp().run()
