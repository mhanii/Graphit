from __future__ import division
from tkinter import *
import tkinter as tk
from matplotlib import *
from matplotlib import pyplot as plt
import numpy as np

import sympy as smp

from sympy import *





root = tk.Tk()
root.title("Graphic Calculator #Credits: Hani#")
root.resizable(0,0)
root.geometry("500x600")
canvas = tk.Canvas(root, width=500, height=600)
canvas.pack()
entry1 = tk.Entry(root,bg="#B4FFF4",bd=1, width=2)
canvas.create_window(120, 400, window=entry1,width=40)
entry2 = tk.Entry(root,bg="#B4FFF4",bd=1, width=2)
canvas.create_window(120, 420, window=entry2,width=40)
calc = tk.Frame(root)

fn = tk.Entry(root, font=('arial',20,'bold') ,bg="#CFF6F7",bd=10, width=30)
canvas.create_text(100,30, text="Write Equation: ", font=('arial', 15,'bold'))
canvas.create_window(250, 100, window=fn)
canvas.create_text(45,400, text="X'nin Max degeri",font=('arial',8,'italic'))
canvas.create_text(45,420, text="Y'nin Max degeri",font=('arial',8,'italic'))

def eqSolve():
    x, y, z, t, b, s = symbols('x y z t b s')
    xm = entry1.get()
    ym = entry2.get()
    xF = int(xm)
    yF = int(ym)
    x = []
    y = []
    s = []

    eq = fn.get()
    for ex in ("log","sin","cos","tan"):
        if ex in eq:
            eq = eq.replace(ex,"np."+ex)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('Graph')
    x = np.linspace(-1 * xF, xF, 10000)
    y = eval(eq)
    plt.ylim(-1 * yF, yF + 1)



    ax.plot(x,y)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    # remove the ticks from the top and right edges
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    print(x)
    print(s)
    plt.show()

button = tk.Button(text="Graph",command=eqSolve,bd=3, bg='#00FFF2',fg='#FF00BD')
canvas.create_window(250, 500, window=button)

root.mainloop()
