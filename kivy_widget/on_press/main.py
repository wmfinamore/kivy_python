from kivy.app import App
from kivy.uix.button import Button


class PressApp(App):
    def show_message(self, instance):
        print("Button pressed!")

    def build(self):
        button = Button(text="Press Me!")
        button.bind(on_press=self.show_message)
        return button


if __name__ == '__main__':
    PressApp().run()
