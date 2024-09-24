from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
grass. draw_now(400, 30)
character.draw_now(100, 90)
x = 100
y = 100
direction = 1
mode = 0

while (True):
    if mode == 0:
        while direction ==1:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x = x+2
            y = (x-100) * 1.5 + 90
            delay(0.02)
            if x > 400:
                direction = 2
        while direction == 2:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x = x + 2
            y = 450 - (x - 400) * 1.5
            delay(0.02)
            if y < 90:
                direction = 3
        while direction == 3 :
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x = x - 2
            y = 90
            delay(0.02)
            if x < 100:
                direction = 1
                mode = 1
    elif mode == 1:
        t = 0
        while t < 360 :
             clear_canvas_now()
             grass.draw_now(400, 30)
             character.draw_now(x, y)
             x = 400 + 200 * math.sin(t/360 * 2 * math.pi)
             y = 300 + 200 * math.cos(t/360 * 2 * math.pi)
             t = t + 1
             delay(0.02)
        mode = 2
        x = 100
        y = 90
    elif mode == 2:
        Rdirection = 0
        x = 50
        y = 90
        Rect = True
        while Rect:
            if Rdirection == 0:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                y += 2
                delay(0.02)
                if  y > 500:
                    Rdirection = 1
            elif Rdirection == 1:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x += 2
                y = 500
                delay(0.02)
                if  x > 750:
                    Rdirection = 2
            elif Rdirection == 2:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                y -= 2
                delay(0.02)
                if  y < 90:
                    Rdirection = 3
            elif Rdirection == 3:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x -=2
                y = 90
                delay(0.02)
                if  x < 50:
                    Rdirection = 1
                    mode = 0
                    Rect = False
            
            
