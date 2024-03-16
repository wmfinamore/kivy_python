from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginApp(App):
    def build(self):
        return LoginScreen()


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'
        self.padding = [50, 100]

        self.username_input = TextInput(hint_text="Username")
        self.add_widget(self.username_input)

        self.passsword_input = TextInput(hint_text="Password", password=True)
        self.add_widget(self.passsword_input)

        self.login_button = Button(text="Login")
        self.login_button.bind(on_release=self.save_credentials)
        self.add_widget(self.login_button)

    def save_credentials(self, instance):
        username = self.username_input.text
        password = self.passsword_input.text

        with open("users.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n",)

        self.clear_inputs()

        # Display a message after saving
        self.add_widget(Label(text="Credentials saved!", font_size=20))

    def clear_inputs(self):
        self.username_input.text = ""
        self.passsword_input.text = ""


if __name__ == '__main__':
    LoginApp().run()
