# Snake Water Gun

import random

lst = ['s', 'w', 'g']
i = 0
youwin = 0
pcwin = 0
while(i<10):
    inp = str(input("enter 's', 'w', 'g' : "))
    res = random.choice(lst)
    if inp=='s' and res=='w':
        youwin = youwin + 1
    elif inp=='w' and res=='g':
        youwin = youwin + 1
    elif inp=='g' and res=='s':
        youwin = youwin + 1
    elif inp=='w' and res=='s':
        pcwin = pcwin + 1
    elif inp=='g' and res=='w':
        pcwin = pcwin + 1
    elif inp=='s' and res=='g':
        pcwin = pcwin + 1
    i = i + 1
print("Game over")
print("you win time", youwin)
print("pc win time", pcwin)