import random, numpy, time
import pyperclip
cooldown = 5 * 60
def evil(c):
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

time.sleep(cooldown)


evil(numpy.random.choice([2]))
