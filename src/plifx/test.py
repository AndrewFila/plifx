import lifxUtil as lu
import time as t
import random as r

TOKEN = 'c36a44cb91da9432817a9ffb0670524036bf1aa5128ee61e8cc7c9586e3f287d'

if __name__ == '__main__':
    lifx = lu.lightUtils(TOKEN)
    ids = lifx.getIDs()
    while(1!=2):
        a = r.randrange(0, 360, 1)
        b = r.randrange(0, 360, 1)
        c = r.randrange(0, 10, 1)/10
        d = r.randrange(0, 10, 1)/10
        lifx.setColor(ids[0], a, d, 1)
        lifx.setColor(ids[1], b, c, 1)
        t.sleep(2)
