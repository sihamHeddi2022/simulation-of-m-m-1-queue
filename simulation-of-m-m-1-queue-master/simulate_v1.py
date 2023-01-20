import numpy as np
import random
import math


def expo(p):
    return (-1/p)*math.log(random.random())


def simulate(lamda, mu, tempsMax):

    #examples = []

    inter_arrival = expo(lamda)
    ct = inter_arrival

    t_arrival = ct

    depart_t = 0

    waiting = []

    nb = {}

    while ct < tempsMax:

        nb[inter_arrival] = inter_arrival/tempsMax
        #print(ct)

        service_time = expo(mu)
        nb[service_time] = service_time/tempsMax

        depart_t = ct +service_time
        #examples.append((t_arrival,depart_t))
        waiting.append(depart_t-t_arrival)

        inter_arrival =  expo(lamda)
        t_arrival = ct + inter_arrival
        if t_arrival < depart_t:
            ct = depart_t
        else:
            ct = t_arrival
    avg_customers = sum(s*nb[s] for s in nb)
    avg_wait = sum(waiting)/len(waiting)
    return avg_wait,avg_customers



print(simulate(6,5,10))





