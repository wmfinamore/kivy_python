from kivy.app import App
from kivy.uix.button import Button


class CustomButton(Button):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.bind(on_disabled=self.on_disabled_event)

    def on_disabled_event(self, instance, value):
        if value:
            print(f"Button {self.text} is now desabled.")
        else:
            print(f"Button {self.text} is now enabled.")


class DisabledApp(App):
    def build(self):
        button = CustomButton(text="Click Me!", size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.bind(on_release=self.toggle_button_state)

        return button

    def toggle_button_state(self, instance):
        instance.disabled = not instance.disabled


if __name__ == '__main__':
    DisabledApp().run()
