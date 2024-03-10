from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window


class ResizingWidget(Widget):
    def __init__(self, **kwargs):
        super(ResizingWidget, self).__init__(**kwargs)
        self.bind(size=self.on_size)

    def on_size(self, instance, new_size):
        self.canvas.clear()  # Clear the canvas ro remove previous rectangle
        with self.canvas:
            Rectangle(pos=self.pos, size=new_size)


class ResizingApp(App):
    def build(self):
        return ResizingWidget()


if __name__ == '__main__':
    ResizingApp().run()
