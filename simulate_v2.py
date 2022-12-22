import numpy as np
import random
import math


def expo(p):
    return (-1/p)*math.log(random.random())





def simulate(lamda, mu, tempsMax):

    t_arrival = expo(lamda)

    ct = t_arrival # current time
    depart = {
        0:[],
        1:[]
    }

    waiting = {
        0:[],
        1:[]
    }

    cm = {
        0:[],
        1:[]
    }

    n1,n2 = 0,0
    w1,W2=0,0
    ans = False

    while ct < tempsMax:

        p = random.random()

        if p!= 2/3:
            depart_t = ct + expo(mu)
            depart[0].append(depart_t)
            if ans:
                pass
        else:
            depart_t = ct + expo(mu)
            depart[1].append(depart_t)
            if ans:
                pass

        ans = True
        if not ans: ct = ct + expo(lamda)

