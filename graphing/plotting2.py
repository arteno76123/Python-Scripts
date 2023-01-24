import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox


def submit(content):
    print(content)

def submit1(content):
    print(content)
    
# something like an empty canvas
figure = plt.figure()

# specification of the left+bottom pos and width + height --> all values between 0 and 1
ax = figure.add_axes([0.2,0.2,0.7,0.7])
ax.set_title("Grafik")

# x and y axis labels
ax.set_xlabel("os x")
ax.set_ylabel("os y")

# add another part - zone for the button
entry_field1 = figure.add_axes([0.2, 0.10, 0.7, 0.05])
text_box = TextBox(entry_field1, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("CHACHACHACHA")

entry_field2 = figure.add_axes([0.2, 0.05, 0.7, 0.05])
text_box2 = TextBox(entry_field2, "Evaluate", textalignment="center")
text_box2.on_submit(submit1)
text_box2.set_val("BUBUBUBU")



ax.plot([1,2,3,4],[4,3,-2,1])  # Plot some data on the axes.

#button_zone = figure.add_axes(1,1,1,1)

plt.show()