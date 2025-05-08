from manim import *

class Thumbnail(Scene):
    def construct(self):

        text1 = Text("From Page to Plot:", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=3, stroke_color=BLACK).scale(1.5).shift(UP*1.5)
        text2 = Text("Christy Anne Jones in Tokyo", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=3, stroke_color=BLACK).scale(1.5).shift(UP*-1.8)
        tb = SurroundingRectangle(text1, color=BLACK, fill_opacity=0.3, buff=0.1, stroke_width=0).rotate(PI)
        tb2 = SurroundingRectangle(text2, color=BLACK, fill_opacity=0.3, buff=0.1, stroke_width=0).rotate(PI)
        pic1 = ImageMobject("japan/thumbnail.png").scale(1.6).shift(UP*0.8)

        self.add(pic1)

        self.add(tb)
        self.add(tb2)
        self.add(text1)
        self.add(text2)



class Australia_Airports(Scene):
    def construct(self):
        class PIN:
            def __init__(self):

                r = 1
                top = Circle(color=RED, radius=r, fill_opacity=1)
                center = Circle(color=WHITE, radius= 0.4 * r, fill_opacity=1)

                top_x = top.get_center()[0]
                top_y = top.get_center()[1]

                a = [r * np.cos(5*PI / 4) + top_x, r * np.sin(5*PI / 4) + top_y, 0]
                b = [r * np.cos(7*PI / 4) + top_x, r * np.sin(7*PI / 4) + top_y, 0]
                c = [top_x, 2.1 * r * np.sin(3*PI / 2) + top_y, 0]

                bottom = ArcPolygon(a, b, c, arc_config={'radius': 3, 'color': RED, }, color=RED, fill_opacity=1)
                self.all = VGroup(bottom, top, center)
                
        pic1 = ImageMobject("japan/australia.png").scale(1.4).shift(UP*1.5)
        adelaide = PIN()
        adelaide.all.shift(LEFT*3.7 + UP*1.3).scale(0.2)
        adelaide_tex = Text("Adelaide Airport", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).next_to(adelaide.all, UP)
        adelaide_tex_b = SurroundingRectangle(adelaide_tex, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        airport1 = VGroup(adelaide.all, adelaide_tex_b, adelaide_tex)

        melbourne = PIN()
        melbourne.all.shift(RIGHT*0.7 + DOWN*1.3).scale(0.2)
        melbourne_tex = Text("Melbourne Airport", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).next_to(melbourne.all, UP)
        melbourne_tex_b = SurroundingRectangle(melbourne_tex, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        airport2 = VGroup(melbourne.all, melbourne_tex_b, melbourne_tex)

        self.play(FadeIn(pic1))
        self.play(pic1.animate.scale(2).shift(LEFT*7 + UP*3.5),run_time=4)
        self.wait(1)
        self.play(Write(airport1),run_time=3)
        self.wait(3)
        self.play(Write(airport2),run_time=3)
        self.wait(1)





class Way_To_Japan(Scene):
    def construct(self):
    
        pic2 = ImageMobject("japan/au-jp.png").scale(1.3)
        plane = ImageMobject("japan/pencilplane.png").scale(0.6)

        self.play(FadeIn(pic2))
        self.wait(1)
        self.play(pic2.animate.scale(5).shift(RIGHT*7 + UP*17),run_time=4)
        self.add(plane)
        self.wait(1)
        self.play(pic2.animate.shift(LEFT*10 + DOWN*28), Rotate(plane, 6*PI), run_time=5)
        self.wait(1)





class Japan_Overview(Scene):
    def construct(self):
        class PIN:
            def __init__(self):

                r = 1
                top = Circle(color=RED, radius=r, fill_opacity=1)
                center = Circle(color=WHITE, radius= 0.4 * r, fill_opacity=1)

                top_x = top.get_center()[0]
                top_y = top.get_center()[1]

                a = [r * np.cos(5*PI / 4) + top_x, r * np.sin(5*PI / 4) + top_y, 0]
                b = [r * np.cos(7*PI / 4) + top_x, r * np.sin(7*PI / 4) + top_y, 0]
                c = [top_x, 2.1 * r * np.sin(3*PI / 2) + top_y, 0]

                bottom = ArcPolygon(a, b, c, arc_config={'radius': 3, 'color': RED, }, color=RED, fill_opacity=1)
                self.all = VGroup(bottom, top, center)

        pic1 = ImageMobject("japan/japan.png").scale(1.5)

        j1 = Text("北海道", font='MS Gothic').shift(UP*3)  
        j2 = Text("Hokkaidō", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).next_to(j1, DOWN*0.7).scale(0.8) 
        j1_b = SurroundingRectangle(j1, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j2_b = SurroundingRectangle(j2, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j1_pin = PIN()
        j1_pin.all.shift(RIGHT*2.5 + UP*3.3).scale(0.2)

        j3 = Text("本州", font='MS Gothic').shift(UP*-1 + RIGHT*2.5)  
        j4 = Text("Honshū", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).next_to(j3, DOWN*0.7).scale(0.8) 
        j3_b = SurroundingRectangle(j3, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j4_b = SurroundingRectangle(j4, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j3_pin = PIN()
        j3_pin.all.shift(RIGHT*0.5 + UP*-0.7).scale(0.2)

        j5 = Text("四国", font='MS Gothic').shift(UP*-2.5 + LEFT*0)  
        j6 = Text("Shikoku", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).next_to(j5, DOWN*0.7).scale(0.8) 
        j5_b = SurroundingRectangle(j5, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j6_b = SurroundingRectangle(j6, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j5_pin = PIN()
        j5_pin.all.shift(LEFT*1.5 + UP*-1.8).scale(0.2)

        j7 = Text("九州", font='MS Gothic').shift(UP*-2.5 + LEFT*4.3)  
        j8 = Text("Kyūshū", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).next_to(j7, DOWN*0.7).scale(0.8) 
        j7_b = SurroundingRectangle(j7, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j8_b = SurroundingRectangle(j8, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j7_pin = PIN()
        j7_pin.all.shift(LEFT*3.2 + UP*-1.8).scale(0.2)

        j9 = Text("東京", font='MS Gothic').shift(UP*0.5 + RIGHT*1.5)  
        j10 = Text("Tōkyō", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).next_to(j9, DOWN*0.7).scale(0.8) 
        j9_b = SurroundingRectangle(j9, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j10_b = SurroundingRectangle(j10, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j9_pin = PIN()
        j9_pin.all.shift(RIGHT*1.5 + UP*-0.7).scale(0.2)

        self.play(FadeIn(pic1))
        self.wait(5)
        self.play(Write(j1_b), Write(j1), Create(j1_pin.all), run_time=3)
        self.play(Write(j2_b), Write(j2))
        self.wait(6)
        self.play(Write(j3_b), Write(j3), Create(j3_pin.all), run_time=3)
        self.play(Write(j4_b), Write(j4))
        self.wait(6)
        self.play(Write(j5_b), Write(j5), Create(j5_pin.all), run_time=3)
        self.play(Write(j6_b), Write(j6))
        self.wait(6)
        self.play(Write(j7_b), Write(j7), Create(j7_pin.all), run_time=3)
        self.play(Write(j8_b), Write(j8))
        self.wait(6)
        self.play(FadeOut(j3_b), FadeOut(j3), FadeOut(j4_b), FadeOut(j4), FadeOut(j3_pin.all))
        self.play(Write(j9_b), Write(j9), Create(j9_pin.all), run_time=3)
        self.play(Write(j10_b), Write(j10))
        self.wait(6)



class Airport_Discussion(Scene):
    def construct(self):
        class PIN:
            def __init__(self):

                r = 1
                top = Circle(color=RED, radius=r, fill_opacity=1)
                center = Circle(color=WHITE, radius= 0.4 * r, fill_opacity=1)

                top_x = top.get_center()[0]
                top_y = top.get_center()[1]

                a = [r * np.cos(5*PI / 4) + top_x, r * np.sin(5*PI / 4) + top_y, 0]
                b = [r * np.cos(7*PI / 4) + top_x, r * np.sin(7*PI / 4) + top_y, 0]
                c = [top_x, 2.1 * r * np.sin(3*PI / 2) + top_y, 0]

                bottom = ArcPolygon(a, b, c, arc_config={'radius': 3, 'color': RED, }, color=RED, fill_opacity=1)
                self.all = VGroup(bottom, top, center)

        pic1 = ImageMobject("japan/tokyo.png").scale(1.5).shift(UP*1.5)

        j1 = Text("羽田空港", font='MS Gothic').shift(LEFT*2.4 + DOWN * 0.3)  
        j2 = Text("Haneda Airport", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).next_to(j1, DOWN*0.7).scale(0.8) 
        j1_b = SurroundingRectangle(j1, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j2_b = SurroundingRectangle(j2, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j1_pin = PIN()
        j1_pin.all.shift(RIGHT*0.3 + DOWN*0.5).scale(0.2)

        j3 = Text("成田空港", font='MS Gothic').shift(RIGHT*3.2 + UP*1.8)  
        j4 = Text("Narita Airport", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).next_to(j3, DOWN*0.8).scale(0.8) 
        j3_b = SurroundingRectangle(j3, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j4_b = SurroundingRectangle(j4, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j3_pin = PIN()
        j3_pin.all.shift(RIGHT*3.2 + DOWN*-0.7).scale(0.2)

        j5 = Text("池袋", font='MS Gothic').shift(UP*1.6)  
        j6 = Text("Ikebukuro", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).next_to(j5, DOWN*0.7).scale(0.8) 
        j5_b = SurroundingRectangle(j5, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j6_b = SurroundingRectangle(j6, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j5_pin = PIN()
        j5_pin.all.shift(UP*0.7).scale(0.2)

        # Draw a line from Haneda to Ikebukuro and show the distance
        haneda_to_ikebukuro_line = Line(start=j1_pin.all[0].get_bottom(), end=j5_pin.all[0].get_bottom(), color=YELLOW)
        distance_text1 = Text("25 km", font='MS Gothic').next_to(haneda_to_ikebukuro_line, LEFT).scale(0.7)
        distance_text1b = SurroundingRectangle(distance_text1, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)

        # Draw a line from Narita to Ikebukuro and show the distance
        narita_to_ikebukuro_line = Line(start=j3_pin.all[0].get_bottom(), end=j5_pin.all[0].get_bottom(), color=YELLOW)
        distance_text2 = Text("65 km", font='MS Gothic').next_to(narita_to_ikebukuro_line, DOWN).scale(0.7)
        distance_text2b = SurroundingRectangle(distance_text2, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)

        self.play(FadeIn(pic1))
        self.wait(3) 
        self.play(Write(j1_b), Write(j1), Create(j1_pin.all), run_time=3)
        self.play(Write(j2_b), Write(j2))
        self.wait(6)
        self.play(Write(j3_b), Write(j3), Create(j3_pin.all), run_time=3)
        self.play(Write(j4_b), Write(j4))
        self.wait(6)
        self.play(FadeOut(j1_b), FadeOut(j1), FadeOut(j2_b), FadeOut(j2), FadeOut(j3_b), FadeOut(j3), FadeOut(j4_b), FadeOut(j4))
        self.wait(1)
        self.play(Write(j5_b), Write(j5), Create(j5_pin.all), run_time=3)
        self.play(Write(j6_b), Write(j6))
        self.wait(6)
        self.play(Create(haneda_to_ikebukuro_line), Write(distance_text1b), Write(distance_text1))
        self.wait(1)
        self.play(Create(narita_to_ikebukuro_line), Write(distance_text2b), Write(distance_text2))
        self.wait(6)



class Train_Route(Scene):
    def construct(self):
        
        pic1 = ImageMobject("japan/nrt-ikebukuro.png").scale(1.5)
        pic2 = ImageMobject("japan/nrt-ikebukuro train.png").scale(1.05)
        self.play(FadeIn(pic1))
        self.play(FadeIn(pic2), FadeOut(pic1))
        self.wait(1)

class Train_Line(Scene):
    def construct(self):

        pic3 = ImageMobject("japan/yamanote.png").scale(1.15)
        pic4 = ImageMobject("japan/gate.png").scale(2.15)
        self.play(FadeIn(pic4))
        self.play(FadeIn(pic3),FadeOut(pic4))
        self.wait(1)

class Konbini(Scene):
    def construct(self):

        pic1 = ImageMobject("japan/konbini inside.jpg").scale(1.35)
        pic2 = ImageMobject("japan/konbini map.png").scale(1.15)

        self.play(FadeIn(pic1))
        self.wait(6)
        self.play(FadeIn(pic2), FadeOut(pic1))
        self.wait(1)

class Tobutojo(Scene):
    def construct(self):

        pic1 = ImageMobject("japan/tobutojo.jpg").scale(2.15)
        self.add(pic1)

class Welcome_To_Nishidai(Scene):
    def construct(self):
        class PIN:
            def __init__(self):

                r = 1
                top = Circle(color=RED, radius=r, fill_opacity=1)
                center = Circle(color=WHITE, radius= 0.4 * r, fill_opacity=1)

                top_x = top.get_center()[0]
                top_y = top.get_center()[1]

                a = [r * np.cos(5*PI / 4) + top_x, r * np.sin(5*PI / 4) + top_y, 0]
                b = [r * np.cos(7*PI / 4) + top_x, r * np.sin(7*PI / 4) + top_y, 0]
                c = [top_x, 2.1 * r * np.sin(3*PI / 2) + top_y, 0]

                bottom = ArcPolygon(a, b, c, arc_config={'radius': 3, 'color': RED, }, color=RED, fill_opacity=1)
                self.all = VGroup(bottom, top, center)

        j1 = Text("西台", font='MS Gothic').shift(LEFT*0 + DOWN * 0)  
        j2 = Text("Nishidai", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).next_to(j1, DOWN*0.7).scale(0.8) 
        j1_b = SurroundingRectangle(j1, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j2_b = SurroundingRectangle(j2, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j1_pin = PIN()
        j1_pin.all.shift(RIGHT*0 + DOWN*1.5).scale(0.4)

        pic1 = ImageMobject("japan/nishidai.png").scale(1.3)
        self.play(FadeIn(pic1))
        self.play(Write(j1_b), Write(j1), Create(j1_pin.all), run_time=3)
        self.play(Write(j2_b), Write(j2))
        self.wait(1)





class Find_Appartment(Scene):
    def construct(self):
        
        pic1 = ImageMobject("japan/book source.jpg").scale(1.3)
        place = Rectangle(height=0.5, width=9, fill_opacity=0).shift(DOWN*0.4 + LEFT*0.5)

        self.play(FadeIn(pic1))
        self.play(Circumscribe(place), run_time=4)





class Christy_And_Book(Scene):
    def construct(self):
        pic1 = ImageMobject("japan/christy.png").scale(1.3)
        pic2 = ImageMobject("japan/book.png").scale(1.3)

        self.play(FadeIn(pic1))
        self.wait(4)
        self.play(FadeOut(pic1), FadeIn(pic2))
        self.wait(1)





class Sign_Investigation(Scene):
    def construct(self):
        pic1 = ImageMobject("japan/sign insta.png").scale(1.3)
        bg = Rectangle(height=4, width=16, fill_opacity=0.8, color=BLACK).shift(DOWN* 2.5)
        j1 = Text("おいしい野菜塾", font='MS Gothic', stroke_width=1, stroke_color=BLACK).shift(DOWN*2.5)
        j1_b = SurroundingRectangle(j1, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)
        j2 = Text("oishii yasai juku", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).shift(DOWN*3.5)
        j2_b = SurroundingRectangle(j2, color=BLACK, fill_opacity=0.7, buff=0.1, stroke_width=0).rotate(PI)

        t1 = Text("delicious", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).shift(DOWN*1.5 + LEFT*3.1)
        t1_b = SurroundingRectangle(t1, color=ORANGE, fill_opacity=0.9, buff=0.1, stroke_width=0).rotate(PI)
        t2 = Text("vegetable", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).shift(DOWN*1.5 + LEFT*0)
        t2_b = SurroundingRectangle(t2, color=GREEN, fill_opacity=0.9, buff=0.1, stroke_width=0).rotate(PI)
        t3 = Text("school", font='Yu Gothic UI', weight="ULTRAHEAVY", stroke_width=1, stroke_color=BLACK).shift(DOWN*1.5 + LEFT*-2.8)
        t3_b = SurroundingRectangle(t3, color=BLUE, fill_opacity=0.9, buff=0.1, stroke_width=0).rotate(PI)

        self.play(FadeIn(pic1))
        self.wait(20)
        self.play(pic1.animate.scale(1.8).shift(UP*2.5 + RIGHT*5.5), FadeIn(bg))
        self.wait(1)
        self.play(Write(j1_b), Write(j1), Write(j2_b), Write(j2))
        self.wait(4)

        self.play(j1[0:4].animate.set_color(ORANGE))
        self.play(Transform(t1_b, t1_b), Transform(j1[0:4].copy(), t1))
        self.wait(4)

        self.play(j1[4:6].animate.set_color(GREEN))
        self.play(Transform(t2_b,t2_b), Transform(j1[4:6].copy(), t2))
        self.wait(4)
        
        self.play(j1[6:].animate.set_color(BLUE))
        self.play(Transform(t3_b,t3_b), Transform(j1[6:].copy(), t3))
        self.wait(6)





class School_Front(Scene):
    def construct(self):
        pic1 = ImageMobject("japan/school front.png").scale(1.3)
        self.add(pic1)

class School_Garden(Scene):
    def construct(self):
        pic1 = ImageMobject("japan/school garden.png").scale(1.05)
        self.add(pic1)

class Meme_Picture(Scene):
    def construct(self):
        pic1 = ImageMobject("japan/same pic.png").scale(1.6)
        pic3 = ImageMobject("japan/cicada.jpg").scale(0.3).shift(UP*2.5 + LEFT*1.5)
        pic2 = ImageMobject("japan/cicada2.png").scale(1.1).rotate(PI).shift(UP*2 + RIGHT*2.3)
        self.add(pic1)
        self.add(pic2)
        self.add(pic3)

class Room(Scene):
    def construct(self):
        pic1 = ImageMobject("japan/room details.png").scale(2.05)
        self.add(pic1)

class Floor_Plan(Scene):
    def construct(self):
        pic1 = ImageMobject("japan/floor plan.png").scale(2.8)
        self.add(pic1)

class Appartment(Scene):
    def construct(self):
        pic1 = ImageMobject("japan/appartment.png").scale(1.5)
        self.add(pic1)

class Rent_Compare(Scene):
    def construct(self):
        pic1 = ImageMobject("japan/suumo jp.jpg").scale(1).shift(LEFT*2.25 + DOWN*1)
        pic2 = ImageMobject("japan/suumo en.jpg").scale(1).shift(LEFT*-3.35 + DOWN*1)
        self.add(pic1)
        self.add(pic2)

class Website(Scene):
    def construct(self):
        pic1 = ImageMobject("japan/website.png").scale(1.1)
        self.add(pic1)

class Ending(Scene):
    def construct(self):

        banner = ManimBanner().scale(0.5)
        bannertxt = Tex("https://www.manim.community/")
        download = Tex("Download Presentation, Script, Code:")
        download2 = Tex("https://github.com/Namitera/English-From-Page-to-Plot-Christy-Anne-Jones-in-Tokyo-09.05.2025").scale(0.8).shift(DOWN*2.5)
        page1 = VGroup(banner,bannertxt,download,download2)

        self.wait()
        self.play(banner.create())
        self.play(banner.expand())
        self.play(banner.animate.to_corner(UL))
        self.play(FadeIn(bannertxt))
        self.play(bannertxt.animate.next_to(banner,DOWN).align_to(banner,LEFT))
        self.wait(1)
        self.play(FadeIn(download))
        self.play(download.animate.to_corner(UL).shift(DOWN*4+LEFT*0.2))
        self.play(FadeIn(download2))
        self.play(download2.animate.shift(UP*0.5))
        self.wait(8)
        self.play(FadeOut(page1))