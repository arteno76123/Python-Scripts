# Fuj program na kreslenie grafu polynomickej funkcie
# Kandidat na prerobenie do OOP

import matplotlib.pyplot as plotter
from matplotlib.widgets import TextBox

# zoznamy hodnot x-iek a y-niek / na zaciatku prazdne
xka = []
yka = []

zaciatok = -5
koniec   =  5

def prepocitaj():
    global xka
    global yka
    skala = 200
    inkrement = (koniec - zaciatok)/skala
    x = zaciatok
    xka = []
    yka = []
    for i in range(skala): 
       xka.append(x)
       y = 7*x**7 - 21*x**5 + x**4 - 12*x +8
       yka.append(y)
       x += inkrement


#######################################   
# zostavenie grafu
#--------------------------------------

def nastav_zaciatok(content):
    global zaciatok
    novy_zaciatok = float(content)
    if zaciatok != novy_zaciatok:
        zaciatok = novy_zaciatok
        prepocitaj()
        kresli_graf()


def nastav_koniec(content):
    global koniec
    novy_koniec = float(content)
    if koniec != novy_koniec:
        koniec = novy_koniec
        prepocitaj()
        kresli_graf()

def kresli_graf():
    # Zapis data do grafu
    global xka
    global yka
    
    # vymaz stary graf
    graf.cla()
    
    # pridaj ciary reprezentujuce os x a y
    graf.axhline(y = 0)
    graf.axvline(x = 0)
    
    # zapis do grafu hodnoty x-iek a y-niek
    graf.plot(xka,yka)
    
    # nastav limity pre zaciatocnu a koncovu hodnotu osi x
    graf.set_xlim(zaciatok, koniec)
    
    # zobraz aktualizovany graf
    plotter.draw()


# vypocitaj uvodne mnoziny hodnot pre graf
prepocitaj()

# vytvorenie prazdneho grafu
platno = plotter.figure()

# vytvorenie prvej zony grafu s poziciou laveho dolneho rohu a rozmerov
# vsetky udaje musia byt medzi 0 a 1
graf = platno.add_axes([0.2,0.3,0.7,0.65])
graf.set_title("Grafika")

# vytvorenie dalsej zony v grafe - tu strcime textboxy
entry_field1 = platno.add_axes([0.2, 0.15, 0.3, 0.1])
text_box = TextBox(entry_field1, "Od: ", textalignment="center")
text_box.on_submit(nastav_zaciatok)
text_box.set_val("-10")

entry_field2 = platno.add_axes([0.6, 0.15, 0.3, 0.1])
text_box2 = TextBox(entry_field2, "Po: ", textalignment="center")
text_box2.on_submit(nastav_koniec)
text_box2.set_val("10")

# vykresli prvu verziu grafu
plotter.show()