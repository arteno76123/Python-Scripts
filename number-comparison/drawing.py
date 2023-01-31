import tkinter

def kresli(filename = r"Z:\IV. FG\Point Files\points0.txt"):
    points = []
    with open(filename) as input_file:
        
        for line in input_file:
            coords = line.split()
            x = int(coords[0])
            y = int(coords[1])
            points.append([x, y])
            
    print(points)

    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, width = 400, height = 300)
    canvas.pack()

    counter = 0
    for point in points:
        x = point[0]
        y = point[1]
        canvas.create_oval(x-2, y-2, x + 2, y + 2)

    canvas.create_line(points)

    window.mainloop()


kresli(r"Z:\IV. FG\Point Files\points4.txt")