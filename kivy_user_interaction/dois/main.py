from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse


class TouchInput(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 0, 0, 1)
            Ellipse(pos=(touch.x - 15, touch.y - 15), size=(30, 30))


class MyApp(App):
    def build(self):
        return TouchInput()


if __name__ == "__main__":
    MyApp().run()
