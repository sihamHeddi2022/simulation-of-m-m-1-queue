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

        p = int(random.randrange(0,3))/3
        depart_t = ct + expo(mu)
        if p!= 2/3:
            n1+=1

            depart[0].append(depart_t)
            if ans:
                if t_arrival < depart[0][len(depart[0]) - 1]:
                    ct = depart[0][len(depart[0]) - 1]
                    waiting[0].append(depart[0][len(depart[0]) - 1] - t_arrival)
                    w1 += 1

                else:
                    ct = t_arrival
                    if len(depart[0]) > 0:
                        depart[0].pop(0)
                        if n1 > 0: n1 += -1
                        if w1 > 0: w1 -= 1
                    cm[0].append(n1 + w1)
        else:
            depart[1].append(depart_t)
            if ans:
                if t_arrival < depart[1][len(depart[1]) - 1]:
                    ct = depart[1][len(depart[1]) - 1]
                    waiting[1].append(depart[1][len(depart[1]) - 1] - t_arrival)
                    W2 += 1
                else:
                    ct = t_arrival
                    if len(depart[1]) > 0:
                        depart[1].pop(0)
                        if n2 > 0: n2 += -1
                        if W2 > 0: W2 -= 1
                    cm[1].append(n2 + W2)

        if not ans: ans = True

        t_arrival = ct + expo(lamda)


    while len(depart[0])>0 :
        depart[0].pop(0)
        if n1 > 0: n1 += -1
        cm[0].append(n1)

    while len(depart[1]) > 0:
        depart[1].pop(0)
        if n2 > 0: n2 += -1
        cm[1].append(n2)

    moy_clien1 = np.mean(cm[0])
    temps_attente1 = np.mean(waiting[0])

    moy_clien2 = np.mean(cm[1])
    temps_attente2 = np.mean(waiting[1])

    return  moy_clien1,temps_attente1,moy_clien2,temps_attente2

moy_clien1,temps_attente1,moy_clien2,temps_attente2 = simulate(5,6,5)

print(moy_clien1,temps_attente1)

print(moy_clien2,temps_attente2)




