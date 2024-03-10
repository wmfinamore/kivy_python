from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.uix.slider import Slider


class ResizingWidget(Widget):
    def __init__(self, **kwargs):
        super(ResizingWidget, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (150, 150)
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size)

    def on_value(self, instance, new_value):
        self.canvas.clear()
        self.size = (new_value, new_value)
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size)


class ValueApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.widget = ResizingWidget()
        self.slider = Slider(min=50, max=300, value=150)
        self.slider.bind(value=self.widget.on_value)
        layout.add_widget(self.widget)
        layout.add_widget(self.slider)
        return layout


if __name__ == '__main__':
    ValueApp().run()
