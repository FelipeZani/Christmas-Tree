import os
import time
import random as rad
def draw(cordef,coranim,corend):# function that draws and colors the tree
    a='* '
    b=' '
    c=30
    print(b*c,"{}{}{}".format(colors["yellow"],a,colors["clean"]))
    for i in range(10):
        if (i!= 1 and i!= 3 and i!= 5 and i!= 7 and i!=9):
            print(b * c, "{}{}{}".format(coranim,a,corend))
        else:
            print(b * c,"{}{}{}".format(cordef,a,corend))
        a+= "* "
        c-=1
    print('                               ||')
    return()

colors={ #library with lights' colors 
    "clean": "\033[m",
    "cyan": "\033[36m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "violet":"\033[35m"
}
os.system('cls')
for i in range(5): #loop that makes the "animation"
    draw(colors["green"],colors["violet"],colors["clean"])
    time.sleep(1)
    os.system('cls')
    draw(colors["green"],colors["cyan"],colors["clean"])
    time.sleep(1)
    os.system('cls')
