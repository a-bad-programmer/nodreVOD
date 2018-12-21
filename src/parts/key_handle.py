import keyboard
import random, numpy, threading

layout = [['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace'],
          ['tab','q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
          ['capslock','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'enter'],
          ['left shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'right shift'],
          ['left ctrl', 'windows', 'alt', 'space','space','space','space','space','right alt','menu','right ctrl']
          ]
amt = 14
keys = []
global lock
lock = threading.Semaphore(1)
global excludes
excludes = []


#keyboard.remap_key('a', 'right shift')
def randkey():
    while True:
        column = numpy.random.randint(len(layout))
        #print(layout[column])
        cell = numpy.random.randint(len(layout[column]))
        #print(cell)
        key = layout[column][cell]
        if key not in excludes:
            lock.acquire()
            excludes.append(key)
            lock.release()
            break
    print(key)
    return key

def findkey(k):
    for row, value in enumerate(layout):
        #print(row)
        for cell, i in enumerate(value):
            if i == k:
                return [row,cell]


def keyswap(k):
    print('A')
    keyboard.unremap_key(k)
    lock.acquire()
    excludes.remove(k)
    lock.release()

def muck(key):
    v, h = findkey(key)
    voff = hoff = 0
    while voff + hoff == 0:
        voff = random.getrandbits(1)
        hoff = random.getrandbits(1)
    voffloc = (v + voff) % len(layout)
    keyboard.remap_key(key, (layout[voffloc][(h + hoff) % len(layout[voffloc])]))
    return key

def listen():

    while True:
        key = muck(randkey())
        while True:
            if(keyboard.is_pressed(key)):
                keyswap(key)
                break

for key in range(amt):
    thread = threading.Thread(target=listen)
    thread.start()
    #print('W')