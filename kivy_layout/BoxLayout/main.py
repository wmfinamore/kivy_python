from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BoxLayoutApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button1 = Button(text="Button 1")
        button2 = Button(text="Button 2")
        button3 = Button(text="Button 3")

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)

        return layout


if __name__ == '__main__':
    BoxLayoutApp().run()
