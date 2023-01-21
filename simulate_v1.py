import random
import math

def expo(p):
    return (-1/p)*math.log(random.random())

def simulate(lamda,mu,closeTime):

    ct = expo(lamda)
    t_arriv = ct



    waiting = False


    response_time = []

    departure = []
    nb = 1

    number_customer_with_time = {
    }

    number_customer_with_time[nb]= ct



    while ct < closeTime:

        depart_t = ct + expo(mu)

        response_time.append(depart_t - t_arriv)
        if nb > 0:
            if waiting :
                departure.append(depart_t)

                if nb not in number_customer_with_time:
                    time = abs(t_arriv - ct)
                else:
                    time = number_customer_with_time[nb] + abs(t_arriv - ct)

                number_customer_with_time[nb] = time

            else:
                if nb not in number_customer_with_time:
                    time = abs(depart_t - ct)
                else:
                    time = number_customer_with_time[nb] + abs(depart_t - ct)

                number_customer_with_time[nb] = time
                nb-=1

        t_arriv = ct + expo(lamda)

        nb += 1



        if t_arriv < depart_t:


            waiting = True
            ct = depart_t

        else:
            if len(departure) > 0 :
                waiting = False
                departure.pop(0)


            ct = t_arriv

    while len(departure)>0:

        if nb not in number_customer_with_time:
            time = abs(departure[0] - ct)
        else:
            time = number_customer_with_time[nb] + abs(departure[0] - ct)

        ct = departure[0]

        number_customer_with_time[nb] = time

        if nb > 0: nb -= 1

        departure.pop(0)
    probability = {s: number_customer_with_time[s]/ct for s in number_customer_with_time}

    avg_customers = sum([s*probability[s] for s in probability])

    avg_response_time = sum(response_time)/len(response_time)

    return avg_customers,avg_response_time

print(simulate(6,5,10))