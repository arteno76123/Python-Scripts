import random

with open(r"Z:\IV. FG\Point Files\points4.txt", "w") as output:
    for i in range(100):
        output.write(f"{random.randint(1, 400)} {random.randint(1, 400)}\n")
    
    