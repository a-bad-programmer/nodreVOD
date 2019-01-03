import keyboard, mouse
import pyperclip, time
import random, numpy, threading
import sys

layout = [['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace'],
          ['tab','q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
          ['capslock','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'enter'],
          ['left shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'right shift'],
          ['left ctrl', 'windows', 'alt', 'space','space','space','space','space','right alt','menu','right ctrl']
          ]
amt = 5
global lock
lock = threading.Semaphore(1)
schlock = threading.Semaphore(1)
global excludes
excludes = []
has_moved = False
#keyboard.remap_key('a', 'right shift')
def randkey():
    while True:
        column = numpy.random.randint(len(layout))
        # print(layout[column])
        cell = numpy.random.randint(len(layout[column]))
        # print(cell)
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


def keyswap(k, pk):
    print('A')
    keyboard.press_and_release(pk)
    schlock.acquire()
    #keyboard.unremap_key(k)
    keyboard.remove_hotkey(k)
    schlock.release()
    lock.acquire()
    excludes.remove(k)
    lock.release()
    muck(randkey())

def muck(key):
    v, h = findkey(key)
    voff = hoff = 0
    while voff + hoff == 0:
        voff = random.getrandbits(1)
        hoff = random.getrandbits(1)
    voffloc = (v + voff) % len(layout)
    pressKey = (layout[voffloc][(h + hoff) % len(layout[voffloc])])
    #keyboard.remap_key(key, (layout[voffloc][(h + hoff) % len(layout[voffloc])]))
    #keyboard.hook_key(key, keyswap(key))
    keyboard.add_hotkey(key, keyswap, args=[key, pressKey],suppress=True)
    return key

def listen():
    while True:
        key = muck(randkey())
        while True:
            if(keyboard.is_pressed(key)):
                keyswap(key)
                break
        print('AAA')


def runMouse(chance):
    while True:
        if (mouse.is_pressed() and not has_moved):
            has_moved = True
            if (numpy.random.randint(chance) == 1):
                mouse.move(numpy.random.randint(20) * numpy.random.choice([-1, 1]),
                           numpy.random.randint(20) * numpy.random.choice([-1, 1]), False,
                           numpy.random.random_sample() * .05)
                print('ran')
        if not mouse.is_pressed():
            has_moved = False
def runMouse2(chance):
    prev_x, prev_y = mouse.get_position()
    while True:
        now_x, now_y = mouse.get_position()
        if abs(now_x-prev_x > 8 and abs(now_y-prev_y) > 5):
            if (numpy.random.randint(chance) == 1):
                mouse.right_click()
        prev_x, prev_y = mouse.get_position()


def runClipboard(cooldown):
    while True:
        time.sleep(cooldown)
        c = numpy.random.choice([1,1,1,1,1,2])
        print('ran clip')
        if c == 1:
            pyperclip.copy('')
        if c == 2:
            dump = pyperclip.paste()
            demp = list(dump)
            a = numpy.random.randint(len(list(dump)))
            b = demp[a]
            c = demp[a - 1 % len(list(dump))]
            demp[a] = c
            demp[a - 1 % len(list(dump))] = b
            pyperclip.copy(''.join(demp))

for key in range(amt):
    muck(randkey())
    '''thread = threading.Thread(target=listen)
    thread.start()
    '''
clipboardThread = threading.Thread(target=runClipboard, args=(5*60,))
#clipboardThread.setDaemon(True)
clipboardThread.start()
time.sleep(.25)
mouseThread = threading.Thread(target=runMouse, args=(10,))
#mouseThread.setDaemon(True)
mouseThread.start()

mouseThread2 = threading.Thread(target=runMouse2, args=(50,))
#mouseThread.setDaemon(True)
mouseThread2.start()
while True:
    pass
