# -*- coding: utf-8 -*-

import simple_draw as sd


def get_polygon(n):
    def draw_shapes(point, angle, length):
        v1 = sd.get_vector(point, angle, length)
        v1.draw()
        end = v1.end_point
        for i in range(n - 1):
            angle += 120 if n == 3 else 360/n
            v = sd.get_vector(end, (angle + 2 if i == n-2 else angle), length)
            v.draw()
            end = v.end_point
    return draw_shapes


draw_triangle = get_polygon(n=10)
draw_triangle(point=sd.get_point(200, 200), angle=26, length=100)

sd.pause()
