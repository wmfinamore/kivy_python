from kivy.app import App
from kivy.uix.button import Button
from kivy.animation import Animation


class MyApp(App):
    def build(self):
        button = Button(text='Clicke Me!')
        button.bind(on_press=self.animate_button)
        return button

    def animate_button(self, instance):
        animation = Animation(size=(100, 20), duration=0.5)
        animation.start(instance)


if __name__ == "__main__":
    MyApp().run()
