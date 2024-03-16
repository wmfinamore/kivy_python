from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.properties import Clock
from kivy.metrics import dp  # dp -> density-independent pixels


class BallApp(App):
    pass


class Build1(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)  # vx -> horizontal velocity
        self.vy = dp(4)  # vy -> vertical velocity

        with self.canvas:
            Color(0, 1, 0)
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))

        Clock.schedule_interval(self.update, 1 / 60)

    def on_size(self, *args):
        print("on_size: " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2)

    def update(self, dt):
        # print("update")
        x, y = self.ball.pos
        x += self.vx
        y += self.vy

        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = self.vy

        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx

        if y < 0:
            y = 0
            self.vy = self.vy

        if x < 0:
            x = 0
            self.vx = self.vx

        self.ball.pos = x, y


BallApp().run()
