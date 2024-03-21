from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        button = Button(text='Click Me!', size_hint=(None, None), size=(200, 50), pos=(100, 100))
        button.bind(on_press=self.on_button_press)
        return button

    def on_button_press(self, instance):
        if instance.text == 'Click Me!':
            instance.text = 'Button Clicked!'
        else:
            instance.text = 'Click Me!'


if __name__ == "__main__":
    MyApp().run()
