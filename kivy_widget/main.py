from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line


class DrawingWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 0, 0) # Set the drawing color to red
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]


class DrawingApp(App):
    def build(self):
        return DrawingWidget()


if __name__ == '__main__':
    DrawingApp().run()
