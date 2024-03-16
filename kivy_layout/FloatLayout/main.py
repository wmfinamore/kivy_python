from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class FloatLayoutApp(App):
    def build(self):
        layout = FloatLayout()
        button1 = Button(text='Button 1', size_hint=(0.2, 0.2), pos_hint={'x': 0.1, 'y': 0.7})
        button2 = Button(text='Button 2', size_hint=(0.3, 0.1), pos_hint={'x': 0.4, 'y': 0.3})
        button3 = Button(text='Button 3', size_hint=(0.15, 0.1), pos_hint={'right': 0.9, 'y': 0.5})

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)

        return layout


if __name__ == '__main__':
    FloatLayoutApp().run()
