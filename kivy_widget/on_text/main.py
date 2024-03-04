from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class TextApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.text_input= TextInput(multiline=False)
        self.text_input.bind(on_text=self.on_text_event)

        layout.add_widget(self.text_input)
        return layout

    def on_text_event(self, instance, value):
        print(f"Real-time text input: {value}")


if __name__ == '__main__':
    TextApp().run()
