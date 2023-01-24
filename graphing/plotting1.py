import matplotlib.pyplot as plotter
import matplotlib as mp
from matplotlib.widgets import TextBox

xka = []
yka = []

zaciatok = float(input())
koniec = float(input())

skala = 200
inkrement = (koniec - zaciatok)/skala
x = zaciatok

for i in range(skala): 
   xka.append(x)
   y = 7*x**7 - 21*x**5 + x**4 - 12*x +8
   yka.append(y)
   x += inkrement

plotter.axhline(y = 0)
plotter.axvline(x = 0)
plotter.plot(xka, yka)
plotter.show()

