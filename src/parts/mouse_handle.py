import mouse
import numpy, random
has_moved = False
chance = 10
while True:
    if (mouse.is_pressed() and not has_moved):
        has_moved = True
        if(numpy.random.randint(chance) == 1):
            mouse.move(numpy.random.randint(20)* numpy.random.choice([-1,1]),numpy.random.randint(20) * numpy.random.choice([-1,1]),False,numpy.random.random_sample()*.05)
            print('ran')
    if not mouse.is_pressed():
        has_moved = False