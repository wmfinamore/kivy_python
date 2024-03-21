from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        button = Button(text='Click Me!')
        button.bind(on_press=self.on_button_click)
        return button

    def on_button_click(self, instance):
        print('Button Clicked!')


if __name__ == '__main__':
    MyApp().run()
