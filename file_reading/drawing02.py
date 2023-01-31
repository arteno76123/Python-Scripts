points = []

with open(r"points0.txt") as source_file:
    for line in source_file:
        coords = line.split()
        x = int(coords[0])
        y = int(coords[1])
        coords = [x, y]
        points.append(coords)

import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width = 400, height = 300)
canvas.pack()

for point in points:
    x, y = point[0], point[1]
    canvas.create_oval(x-2, y-2, x+2, y+2)

canvas.create_line(points)
window.mainloop()