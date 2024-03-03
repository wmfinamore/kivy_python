from kivy.app import App
from kivy.uix.button import Button


class ReleaseApp(App):
    def show_message(self, instance):
        print("Button released!")

    def build(self):
        button = Button(text="Presse and Released Me!")
        button.bind(on_release=self.show_message)
        return button


if __name__ == '__main__':
    ReleaseApp().run()
