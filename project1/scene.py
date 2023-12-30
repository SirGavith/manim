from manim import *
from pyrr import Vector3


class SetLatex(ThreeDScene):
    def construct(self):
        text = MathTex('a^2 + b^2 = c^2')
        self.add(text)

        text = MathTex('\int_{a}^{b}f(x)dx=F(b)-F(a)')
        text.set_y(-1)
        self.add(text)

        text = MathTex('\double_int{R}f(x)dx=')
        text.set_y(-2)
        self.add(text)