from kivy.app import App
from kivy.uix.button import Button


class MyButton(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print('Button Clicked!')
            return True
        return super(MyButton, self).on_touch_down(touch)


class MyApp(App):
    def build(self):
        return MyButton(text='Click Me!')


if __name__ == '__main__':
    MyApp().run()
