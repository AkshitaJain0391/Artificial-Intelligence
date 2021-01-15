# Example of world building, display, and successor computation for the artificial 
# intelligence path-finding lab
#
# Author: Didier Lime  and Akshita Jain 
# Date: 2018-10-03

from random import random
from sys import stdout

class world:
    # initialise the world
    # L is the number of columns
    # H is the number of lines
    # P is the probability of having a wall in a given tile
    def __init__(self, L, H, P):
        self.L = L  # c
        self.H = H  # r

        # the world is represented by an array with one dimension
        self.w = [0 for i in range(L*H)] # initialise every tile to empty (0)

        # add walls in the first and last columns
        for i in range(H):
            self.w[i*L] = 1
            self.w[i*L+L-1] = 1
        
        # add walls in the first and last lines
        for j in range(L):
            self.w[j] = 1
            self.w[(H-1)*L + j] = 1

        for i in range(H):
            for j in range(L):
                # add a wall in this tile with probability P and provided that it is neither
                # the starting tile nor the goal tile 
                if random() < P and not (i == 1 and j == 1) and not (i == H-2 and j == L-2):
                    self.w[i*L+j] = 1

    # display the world
    def display(self):
        for i in range(self.H):
            for j in range(self.L):
                if self.w[i * self.L + j] == 0:
                    stdout.write('.')
                elif self.w[i * self.L + j] == 1:
                    stdout.write('W')

            print('')

    # display the path
    def displayPath(self, s0, t, path):

        for i in range(self.H):
            for j in range(self.L):
                if self.w[i * self.L + j] == 0:
                    coord = i * self.L + j
                    if coord in path:
                        stdout.write('P')
                    elif coord == s0:
                        stdout.write('S')
                    elif coord == t:
                        stdout.write('F')
                    else:
                        stdout.write('.')
                elif self.w[i * self.L + j] == 1:
                    stdout.write('W')

            print('')

    # compute the successors of tile number i in world w
    def successors(self, i):
        if i < 0 or i >= self.L * self.H or self.w[i] == 1:
            # i is an incorrect tile number (outside the array or on a wall)
            return [] 
        else:
            # look in the four adjacent tiles and keep only those with no wall
            return list(filter(lambda x: self.w[x] != 1, [i - 1, i + 1, i - self.L, i + self.L]))

    # Depth-first search
    # starting from tile number s0, find a path to tile number t
    # return (r, path) where r is true if such a path exists, false otherwise
    # and path contains the path if it exists  
    def dfs(self, s0, t):
        r = False
        path = []
        
        # ... Complete here ...

        return (r, path)

    def stw(self, s0, t):
        map = {}  # initialize map
        path = []  # path in backward direction
        r = False
        P = []
        W = [s0]
        while len(W) > 0 and not r:
            s = W[-1]  # get the last element of W
            W.pop()
            if s == t:
                print("Bingooooooooooooo")
                r = True
            else:
                P.insert(0, s)  # insert s to P 
                for succ_s in self.successors(s):
                    if (succ_s not in P) and (succ_s not in W):
                        map[succ_s] = s
                        W.insert(0, succ_s)
        if r is True:
            pred = map[t]
            while pred != s0:
                path.append(pred)
                # get new predessor
                pred = map[pred]
                
        return (r, path)



# create a world
w = world(20, 10, 0.2)

# display it 
w.display()

# print the tile numbers of the successors of the starting tile (1, 1)
print(w.successors(w.L + 1))

s0 = 0

t = 0

for i in range(w.L*w.H):
    if w.w[i] == 0:
        s0 = i
        break;

for i in range(w.L*w.H):
    if w.w[i] == 0 and i > 5 * s0:
        t = i
        break;
print("s0 = ", s0)
print("t =", t)

r, path = w.stw(s0, t)
if r is True:
    print("found path")
    print("path: ", path)
    w.displayPath(s0, t, path)
else:
    print("not found path")
