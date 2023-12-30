from manim import *

def plus(w,v):
    return [w[0]+v[0],w[1]+v[1],w[2]+v[2]]
def proj(v,e):
    return [0 if e==0 else v[0],0 if e==1 else v[1],0 if e==2 else v[2]]

class ParallelogramProjections(ThreeDScene):
    def construct(self):
        # circle = Circle()  # create a circle
        # circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        # self.play(Create(circle))  # show the circle on screen

        xz_poslist = [
            [-5,0,5],
            [5,0,5],
            [5,0,-5],
            [-5,0,-5],
        ]
        xz_plane = Polygon(*xz_poslist, color=WHITE)
        xz_plane.set_fill(WHITE, opacity=0.5)
        xy_poslist = [
            [-5,5,0],
            [5 ,5,0],
            [5 ,-5,0],
            [-5,-5,0],
        ]
        xy_plane = Polygon(*xy_poslist, color=WHITE)
        xy_plane.set_fill(WHITE, opacity=0.5)

        yz_poslist = [
            [0,-5,5],
            [0,5 ,5],
            [0,5 ,-5],
            [0,-5,-5],
        ]
        yz_plane = Polygon(*yz_poslist, color=WHITE)
        yz_plane.set_fill(WHITE, opacity=0.5)


        self.set_camera_orientation(phi=2*PI/5, theta=PI/7)
        self.begin_ambient_camera_rotation(0.05)


        axes = ThreeDAxes()
        labels = axes.get_axis_labels(
            Text("x-axis").scale(0.5),
            Text("y-axis").scale(0.5),
            Text("z-axis").scale(0.5)
        )
        self.add(axes, labels)
        


        v = [1, 0,-2]
        w = [0, 1,-1]

        o = [1,1,4]

        pos_list = [
            o,
            plus(o,v),
            plus(plus(o,w),v),
            plus(o,w),
        ]

        parallelogram = Polygon(*pos_list, color=PURPLE_B)
        parallelogram.set_fill(PINK, opacity=0.6)


        self.play(Create(parallelogram.copy()))




        # project to xz plane

        self.play(FadeIn(xz_plane))

        new_pos_list = [ proj(p,1) for p in pos_list ]

        parallelogram2 = Polygon(*new_pos_list, color=PURPLE_B)
        parallelogram2.set_fill(PINK, opacity=0.8)

        self.play(Transform(parallelogram.copy(), parallelogram2))
        # self.wait(duration=1)

        self.play(FadeOut(xz_plane))



        #project to yz plane

        self.play(FadeIn(yz_plane))


        new_pos_list2 = [ proj(p,0) for p in pos_list ]

        parallelogram2 = Polygon(*new_pos_list2, color=PURPLE_B)
        parallelogram2.set_fill(PINK, opacity=0.8)

        self.play(Transform(parallelogram.copy(), parallelogram2))
        # self.wait(duration=1)


        self.play(FadeOut(yz_plane))


        #project to xy plane

        self.play(FadeIn(xy_plane))


        new_pos_list2 = [ proj(p,2) for p in pos_list ]

        parallelogram2 = Polygon(*new_pos_list2, color=PURPLE_B)
        parallelogram2.set_fill(PINK, opacity=0.8)

        self.play(Transform(parallelogram.copy(), parallelogram2))
        # self.wait(duration=1)


        self.play(FadeOut(xy_plane))

        self.wait(duration=2)

        self.play(FadeIn(xy_plane),FadeIn(xz_plane),FadeIn(yz_plane))
