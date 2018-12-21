import mouse
import numpy, random
has_moved = False
while True:
    if (mouse.is_pressed() and not has_moved):
        has_moved = True
        mouse.move(numpy.random.randint(15),numpy.random.randint(15) * numpy.random.choice([-1,1]),False,numpy.random.random_sample()*.05)
    if not mouse.is_pressed():
        has_moved = False