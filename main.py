import numpy as np
import pandas as pd
import random
import math


def expo(p):
    return (-1/p)*math.log(random.random())


def simulate(lamda, mu, tempsMax):

    t_arrival = expo(lamda)
    w,s=0 , 0  # number of customer waiting , number of customer served à l'instant t
    waiting = [] # waiting time of each customer
    depart = [] # departed time of each customer
    cm = [] # the number of customers in station ( served + waiting ) à l'instant t
    ct = t_arrival # current time


    while ct < tempsMax:

        depart_t = ct + expo(mu)
        t_arrival = ct + expo(lamda)

        depart.append(depart_t)

        if t_arrival < depart[0]:


            waiting.append(depart_t - t_arrival)
            w+=1

        else:

            if len(depart)>0:
                depart.pop(0)
                s+=1
                if w>0 : w+=-1
                cm.append(s+w)

        ct = t_arrival

    while len(depart)>0 :
        depart.pop(0)
        s+=1
        w-=1
        cm.append(s+w)

simulate(5,6,5)














