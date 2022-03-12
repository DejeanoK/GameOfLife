import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

CYCLE = 1000
def step(Board):
    b = Board.astype(int)
    neigh = np.zeros(b.shape)
    neigh[1:-1, 1:-1] = (b[:-2, :-2]  + b[:-2, 1:-1] + b[:-2, 2:] +
                         b[1:-1, :-2] +                b[1:-1, 2:]+
                         b[2:, :-2]   + b[2:, 1:-1]  + b[2:, 2:])
    return np.logical_or(neigh == 3, np.logical_and(b == 1, neigh == 2)).astype(int)

def live(Board):
    hist = np.zeros((CYCLE,Board.shape[0], Board.shape[1]),dtype=int)
    for i in range(CYCLE):
        hist[i] = Board
        Board = step(Board)
    return hist

def animate(i):
    im.set_data(hist[i,:,:])
    return im,

def readFile(path,shift = (0,0), customSize=(500,500)):
    res = 0
    maxY = 0
    maxX = 0
    patterns = np.zeros(shape=customSize)
    file = open(path, "r")
    for x,line in enumerate(file):
        if line[0] == '!':
            res += 1
            continue
        for y,c in enumerate(line):
            if c == 'O':
                patterns[x-res,y] = 1
            if y > maxY:
                maxY = y
        maxX = x
    board = np.zeros(shape = customSize)
    board[shift[0]:shift[0] + maxX, shift[1]:shift[1] + maxY] = np.array(patterns[:maxX, :maxY])
    return board

def fig_56p27():
    return readFile("patterns/56p27.txt", (20,20),(100,100))

def fig_233p3h1v0():
    return readFile("patterns/233p3h1v0.txt", (50,50), (150,150))

def fig_phoenix():
    return readFile("patterns/phoenix1.txt",(15,15), (50,50))

def fig_garden():
    return readFile("patterns/gardenofeden1.txt", (15, 15), (100,50))

def fig_3engine():
    return readFile("patterns/3engine.txt", (50, 50), (500,500))

def fig_sidecar():
    return readFile("patterns/sidecargun.txt", (50, 50), (500,500))

b = fig_sidecar()
hist = live(b)

fig = plt.figure(figsize=(16, 9), dpi=120)
plt.axis('off')
im = plt.imshow(b, cmap="binary")

anim = animation.FuncAnimation(fig, animate, repeat=False, interval = 50, frames = CYCLE)
plt.show()
