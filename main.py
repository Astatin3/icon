import drawsvg as draw
import math


GREEN = '#00ff00'
BLACK = '#000000'
WHITE = '#ffffff'

#crop = (210/256)
crop= 1
size = 4096 / crop
d = draw.Drawing(size*2*crop, size*2*crop, origin='center')

d.append(draw.Rectangle(-size*crop, -size*crop, size*2*crop ,size*2*crop, fill=BLACK))

def draw_oct(r:float, c):
    r += r-r*math.sin(math.pi*0.625)

    lines = []
    for i in range(0,9):
        lines.append(r*math.cos((math.pi/4)*i + math.pi/8))
        lines.append(r*math.sin((math.pi/4)*i + math.pi/8))

    d.append(draw.Lines(0,0, *lines,
    close=True,
    fill=c))


draw_oct(size*(211/256),GREEN)
draw_oct(size*(193/256),BLACK)


r1 = size*(14/256)
r2 = size*(80/128)
r3 = size*(88/128)
r4 = size*(2/256)


lines = []


lines.append((r2+r4)*math.cos(-math.pi/2))
lines.append((r2+r4)*math.sin(-math.pi/2))

lines.append((r3+r4)*math.cos(math.pi*(11/6)))
lines.append((r3+r4)*math.sin(math.pi*(11/6)))

lines.append((r2+r4)*math.sin(math.pi*(2/6)))
lines.append((r2+r4)*math.cos(math.pi*(2/6)))

lines.append((r3+r4)*math.cos(math.pi*(3/6)))
lines.append((r3+r4)*math.sin(math.pi*(3/6)))

lines.append((r2+r4)*math.cos(math.pi*(5/6)))
lines.append((r2+r4)*math.sin(math.pi*(5/6)))

lines.append((r3+r4)*math.cos(math.pi*(7/6)))
lines.append((r3+r4)*math.sin(math.pi*(7/6)))



d.append(draw.Lines(lines[0],lines[1], *lines,
close=True,
fill=GREEN))

def draw_d(rot:float):
    lines = []

    lines.append(r1*math.cos(rot))
    lines.append(r1*math.sin(rot))

    lines.append(r3*math.cos(rot + math.pi/3))
    lines.append(r3*math.sin(rot + math.pi/3))

    lines.append(r2*math.cos(rot))
    lines.append(r2*math.sin(rot))

    lines.append(r3*math.cos(rot - math.pi/3))
    lines.append(r3*math.sin(rot - math.pi/3))

    d.append(draw.Lines(lines[0],lines[1], *lines,
    close=True,
    fill=BLACK))

draw_d(-math.pi/2)
draw_d(math.pi*(1/6))
draw_d(math.pi*(5/6))

d.save_png('icon.png')



# import cv2

# img1 = cv2.imread("example.png")
# img2 = cv2.imread("Astatin3-v4.png")

# cv2.imwrite("diff.png", img1+img2)
