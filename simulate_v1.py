import numpy as np
import random
import math


def expo(p):
    return (-1/p)*math.log(random.random())


def simulate(lamda, mu, tempsMax):

    t_arrival = expo(lamda)
    waiting = [] # waiting time of each customer
    depart = [] # departed time of each customer
    cm = [] # the number of customers in station ( served + waiting ) à l'instant t
    ct = t_arrival # current time

    n , w = 0,0  # number of customers arrived

    while ct < tempsMax:

        depart_t = ct + expo(mu)
        t_arrival = ct + expo(lamda)

        depart.append(depart_t)
        n += 1

        if t_arrival < depart[0]:
            ct = depart[0]

            waiting.append(depart[len(depart)-1] - t_arrival)
            w+=1

        else:

            if len(depart)>0:
                depart.pop(0)
                if n>0 :n+=-1
                if w > 0 : w-=1
        cm.append(n + w)
        ct = t_arrival



    while len(depart)>0 :
        depart.pop(0)
        if n > 0: n += -1
        cm.append(n)

    moy_clien = np.mean(cm)
    temps_attente = np.mean(waiting)

    return moy_clien,temps_attente



moy_clien,temps_attente = simulate(5,6,5)

print("le nombre moyenne du client dans la station est : ",int(moy_clien))
print("le temps d'attente moyenne dans le guichet est : ",temps_attente)










