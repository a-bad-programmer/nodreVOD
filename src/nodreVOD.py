import random, numpy, keyboard, mouse, time, pyperclip, threading
layout = [['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace'],
          ['tab','q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
          ['capslock','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'enter'],
          ['left shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'right shift'],
          ['left ctrl', 'windows', 'alt', 'space','space','space','space','space','right alt','menu','right ctrl']
          ]

keyboardOdds = .5
missClickChance = 10
clipClearCooldown = 5*60
randomDragChance = 50
has_moved = False




def randkey():
    cell = numpy.random.randint(0,len(layout))
    collum = random.randint(0,len(layout[cell]))
    return cell, collum

def missClickOLD(chance):
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

def missClick(chance):
    if (random.uniform(0, 100) < chance):
        mouse.move(numpy.random.randint(20) * numpy.random.choice([-1, 1]),
                   numpy.random.randint(20) * numpy.random.choice([-1, 1]), False,
                   numpy.random.random_sample() * .05)
        print('ran')


def randomDrag(chance):
    #prev_x, prev_y = mouse.get_position()
    #while True:
        """now_x, now_y = mouse.get_position()
        if abs(now_x-prev_x > 8 and abs(now_y-prev_y) > 5):
            if (numpy.random.randint(chance) == 1):
                mouse.right_click()"""
        #prev_x, prev_y = mouse.get_position()


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


def muck(event):
    #print("Name: " + event.name)
    #print(event.name == 'a')
    cell = collum = -1
    for x in range(len(layout)):
        for y in range(len(layout[x])):
            #print(layout[x][y])
            if (layout[x][y] == event.name):
                cell = x
                collum = y
    #if(cell or collum == -1):
     #   exit("no ifnd")


    if(random.uniform(0,100) < keyboardOdds):
        randKey = layout[cell + numpy.random.randint(-1,1)][collum + numpy.random.randint(-1,1)]
        keyboard.press(randKey)
        keyboard.release(randKey)
    else:
        keyboard.press(event.name)

def main():
    """for i in range(amt):
        a,b = randkey()
        initBind(a,b)
        print("A " + a)
        print("B " + b)"""
    clipboardThread = threading.Thread(target=runClipboard, args=(clipClearCooldown,))
    # clipboardThread.setDaemon(True)
    clipboardThread.start()
    #mouseThread = threading.Thread(target=missClick, args=(missClickChance,))
    # mouseThread.setDaemon(True)
    #mouseThread.start()

    #mouseThread2 = threading.Thread(target=randomDrag, args=(randomDragChance,))
    # mouseThread.setDaemon(True)
    #mouseThread2.start()
    mouse.on_click(missClick, [missClickChance])
    keyboard.on_press(muck, True)
    keyboard.wait()



if(__name__ == "__main__"):
    main()