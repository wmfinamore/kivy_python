from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class StackLayoutApp(App):
    def build(self):
        layout = StackLayout(orientation='tb-lr', spacing=10, padding=10)
        # tb-lr -> top to bottom and left to right

        button1 = Button(text="Button 1", size_hint=(None, None), size=(150, 50))
        button2 = Button(text="Button 2", size_hint=(None, None), size=(160, 60))
        button3 = Button(text="Button 3", size_hint=(None, None), size=(100, 70))

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)

        return layout


if __name__ == '__main__':
    StackLayoutApp().run()
