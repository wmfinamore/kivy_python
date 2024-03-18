from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class MyCanvas(Widget):
    def __init__(self, **kwargs):
        super(MyCanvas, self).__init__(*kwargs)

        with self.canvas:
            Color(1, 0, 0, 1)  # Set color to red
            Rectangle(pos=(100, 100), size=(200, 200))


class MyApp(App):
    def build(self):
        return MyCanvas()


if __name__ == "__main__":
    MyApp().run()
