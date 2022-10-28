from typing_extensions import runtime
from manim import *

depo = "/Users/dogukanturkoz/Documents/manim/media/images/lale"


class armut(Scene):
    def construct(self):
        self.add_sound(sound_file="/Users/dogukanturkoz/Documents/manim/media/music/120.mov")

        def birbolux(x):
            return(1 / x)

        axes1 = Axes(
            x_range=[
                0, 5], x_length=3, y_range=[
                0, 2, 0.25], y_length=5, axis_config={"include_numbers": True}, tips=False)

        plane1 = NumberPlane(
            x_range=[
                0, 5], x_length=3, y_range=[
                0, 2, 0.25], y_length=5)

        grafbir = plane1.plot(lambda x: 1 / x, x_range=[0.5, 5])

        label1 = axes1.get_graph_label(grafbir, "\\frac{1}{x}")
        self.play(Write(axes1, lag_ratio=0.01, run_time=1))
        self.play(DrawBorderThenFill(plane1))

        for i in range(1, 5):
            self.play(Create(Dot(point=plane1.c2p(i, birbolux(i), 0), color=YELLOW)))

        self.wait(1)
        self.play(Create(grafbir))
        self.play(FadeIn(label1))
        self.wait(1)

        birlimit = MathTex(
            r" \lim_{x \to \infty} \frac{1}{x} = 0",
            color=WHITE).shift(RIGHT * 4.5)
        self.play(Write(birlimit))
        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        ####

        def ikix(x):
            return(2 * x / (x + 2))

        axes2 = Axes(
            x_range=[
                0, 5], x_length=3, y_range=[
                0, 2, 0.25], y_length=5, axis_config={"include_numbers": True}, tips=False)

        plane2 = NumberPlane(
            x_range=[
                0, 5], x_length=3, y_range=[
                0, 2, 0.25], y_length=5)

        grafiki = plane2.plot(lambda x: 2 * x / (x + 2), x_range=[0, 5])

        label2 = axes2.get_graph_label(grafiki, "\\frac{2x}{x+2}")
        self.play(Write(axes2, lag_ratio=0.01, run_time=1))
        self.play(DrawBorderThenFill(plane2))

        for i in range(1, 5):
            self.play(Create(Dot(point=plane2.c2p(i, ikix(i), 0), color=YELLOW)))

        self.wait(1)
        self.play(Create(grafiki))
        self.play(FadeIn(label2))
        self.wait(1)

        birlimit = MathTex(
            r" \lim_{x \to \infty} \frac{2x}{x+2} = \; ?",
            color=WHITE).shift(RIGHT * 4.5)
        self.play(Write(birlimit))
        self.wait(4)
        birlimitq = MathTex(
            r" \lim_{x \to \infty} \frac{2x}{x+2} = 2",
            color=WHITE).shift(RIGHT * 4.5)
        self.play(Transform(birlimit, birlimitq))
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        ####

        text0 = Text("Faydalı bir eşitlik:").shift(UP * 1.6).scale(0.8)
        text = MathTex(r"1^2 + 2^2 + 3^2 + ... + n^2 = \frac{n(n+1)(2n+1)}{6}")

        self.play(Write(text0), run_time=2)
        self.play(Write(text), run_time=2)
        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        formulbir = MathTex(r"\int_{0}^{a} x^2 \,dx = \; ? ").scale(2)
        self.play(Write(formulbir), run_time=2)
        self.wait(2)
        self.play(FadeOut(formulbir))
        axes = Axes(
            x_range=[
                0, 6], x_length=2, y_range=[
                0, 25, 2], y_length=5, axis_config={"include_numbers": True}, tips=False)

        plane = NumberPlane(
            x_range=[
                0, 6], x_length=2, y_range=[
                0, 25, 2], y_length=5)

        parab = always_redraw(lambda: plane.plot(lambda x: x**2, x_range=[0, 5]))
        #labelcik = axes.get_graph_label(parab, "x^2")

        area = plane.get_riemann_rectangles(graph=parab, dx=0.8)
        area1 = plane.get_riemann_rectangles(graph=parab, dx=0.4)
        area2 = always_redraw(lambda: plane.get_riemann_rectangles(graph=parab, dx=0.2))

        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        self.play(DrawBorderThenFill(plane))
        self.play(Create(parab))
        # self.play(FadeIn(labelcik))
        self.play(Create(area))
        self.wait()
        self.play(Transform(area, area1))
        self.wait()
        self.play(Transform(area1, area2))
        self.wait()
        # self.play(plane.animate.shift(RIGHT * 4))
        # self.play(area2.animate.shift(RIGHT * 4))

        #im = ImageMobject(f"{depo}/riemann.jpg").scale(3)

        # self.play(FadeIn(im), run_time=3)
        # self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        diksay = MathTex(r"\text{Dikdörtgen sayısını } n \text{ ile gösterelim.}",
                         color=GREEN).shift(UP * 2.2)
        dikalan = Text(
            "Dikdörtgenlerin alanları toplamı:",
            font_size=35,
            color=WHITE).shift(
            UP * 1.2)
        bir = MathTex(
            r"\left(\frac{a}{n}\right)\left(\frac{a}{n}\right)^2+\left(\frac{a}{n}\right)\left(\frac{2a}{n}\right)^2+\left(\frac{a}{n}\right)\left(\frac{3a}{n}\right)^2+ \cdots + \left(\frac{a}{n}\right)\left(\frac{na}{n}\right)^2",
            color=BLUE).scale(0.75)

        ilkyazilar = VGroup(diksay, dikalan, bir)
        self.play(Write(ilkyazilar))
        self.wait(2)
        self.play(FadeOut(diksay))
        self.play(FadeOut(dikalan))
        self.play(bir.animate.shift(UP * 2.5))
        self.wait()
        iki = MathTex(
            r"=\left(\frac{a}{n}\right)\left(\frac{a}{n}\right) ^ 2 +\left(\frac{a}{n}\right)4\left(\frac{a}{n}\right) ^ 2 +\left(\frac{a}{n}\right)9\left(\frac{a}{n}\right) ^ 2 + \cdots + \left(\frac{a}{n}\right)n ^ 2\left(\frac{a}{n}\right) ^ 2",
            color=BLUE).scale(0.75).shift(UP)
        self.play(Write(iki))
        self.wait()

        uc = MathTex(
            r"=\left(\frac{a}{n}\right) ^ 3(1 ^ 2 + 2 ^ 2 + \cdots + n ^ 2)",
            color=BLUE).scale(0.75).shift(DOWN * 0.5)
        dort = MathTex(
            r"=\left(\frac{a}{n}\right) ^ 3\frac{n(n + 1)(2n + 1)}{6}",
            color=BLUE).scale(0.75).shift(DOWN * 2)
        bes = Text(
            "Dikdörtgen sayısını sonsuza götürdüğümüzde: ",
            color=WHITE).shift(UP).scale(0.7)
        alti = MathTex(
            r" \lim_{n \to \infty} \left( \frac{a}{n} \right) ^ 3 \frac{n(n + 1)(2n + 1)}{6} =  ", r" \frac{a^3}{3}",
            color=BLUE).shift(DOWN * 0.5)
        alti.set_color_by_tex(r" \frac{a^3}{3}", RED)
        surroundingRectangle = SurroundingRectangle(mobject=alti[1], color=YELLOW, buff=0.15)

        self.play(Write(uc))
        self.wait()
        self.play(Write(dort))
        self.wait()
        self.play(FadeOut(bir, iki, uc, dort), runtime=3)
        self.play(Write(bes))
        self.wait()
        self.play(Write(alti))
        self.play(Create(surroundingRectangle))
        self.wait(2)
