from turtle import circle
from typing_extensions import runtime
from manim import *
from random import *

import random
from manim import *
import math

r = 3


def gen_coor(x, y, rad):
    while True:
        a = random.random() * 2 * rad - rad
        b = random.random() * rad * 2 - rad
        if math.sqrt(a**2 + b**2) < rad:
            break
    return [a + x, b + y, 0]

    # else:
    #     return gen_coor(x, y, rad)


class armut(Scene):
    def construct(self):
        self.add_sound(sound_file="/Users/dogukanturkoz/Documents/manim/media/music/27jazz.mov")
        cembercik = Circle(radius=r, color=PURPLE)
        self.play(Create(cembercik))
        self.play(Flash(
            cembercik, line_length=1,
            num_lines=30, color=RED,
            flash_radius=r + SMALL_BUFF,
            time_width=0.3, run_time=2,
            rate_func=rush_from
        ))
        listecik = VGroup()
        palet = [RED, BLUE, GREEN, PURPLE, PINK, WHITE, LIGHT_BROWN, TEAL, YELLOW, GOLD, MAROON]

        l = 5
        for i in range(l):
            bir_kose = Dot(gen_coor(1, 1, 0.9), color=palet[i % len(palet)])
            listecik.add(bir_kose)

        for i in range(l):
            obur_kose = Dot(gen_coor(-1, -1, 0.9), color=palet[i % len(palet)])
            listecik.add(obur_kose)

        n = 90
        animeliste = []
        for i in range(n):
            koray_noktasi = (Dot(gen_coor(0, 0, 3), color=palet[i % len(palet)]))
            listecik.add(koray_noktasi)
            #self.play(Create(koray_noktasi), runtime=0.1)
            #self.play(Flash(koray_noktasi), time_width=0.1)
            # self.play(FadeIn(koray_noktasi))
        for i in range(n):
            animeliste.append(Create(listecik[i]))
            animeliste.append(Flash(listecik[i], color=palet[i % len(palet)]))

        random.shuffle(listecik)
        self.play(AnimationGroup(*animeliste, lag_ratio=0.1))
        self.wait()
        listecik.save_state()
        self.play(listecik.animate.arrange_in_grid(rows=10, columns=10))

        colors = [RED, "#ffd166", "#06d6a0", BLUE]
        all_colors = color_gradient(colors, n + 2 * l)
        self.play(
            AnimationGroup(
                *[s.animate.set_color(all_colors[i]) for i, s in enumerate(listecik)],
                lag_ratio=0.02,
            )
        )
        self.wait(2)
        # # def color_updater(obj):
        # #     for s in listecik:
        # #         for i in listecik:
        # #             obj.set_color(all_colors[i])

        # # listecik.add_updater(color_updater)

        self.play(Restore(listecik), run_time=2)
        # # swaps = 25
        # # speed_start = 0.8
        # # speed_end = 0.1

        # # for i in range(swaps):
        # #     speed = speed_start - abs(speed_start - speed_end) / swaps * i

        # #     # pick two random circles (ensuring a != b)
        # #     a, b = sample(range(n), 2)

        # #     # swap with a slightly larger arc angle
        # #     self.play(
        # #         Swap(listecik[a], listecik[b]), run_time=speed,
        # #     )
