from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GridLayoutApp(App):
    def build(self):
        layout = GridLayout(cols=3, spacing=10, padding=10)
        button1 = Button(text="Button 1")
        button2 = Button(text="Button 2")
        button3 = Button(text="Button 3")
        button4 = Button(text="Button 4")

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)

        return layout


if __name__=='__main__':
    GridLayoutApp().run()
