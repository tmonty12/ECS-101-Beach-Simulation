import numpy as np
import random
import time
from part3 import cafeshop

def optimizer():
    la1 = eval(input("Enter the location of A1: "))
    ca1 = eval(input("Enter the price of one cup of coffee at A1: "))
    la2 = eval(input("Enter the location of A2: "))
    ca2 = eval(input("Enter the price of one cup of coffee at A2: "))
    trials = 100000

    profitA1, profitA2 = cafeshop(trials, la1, ca1, la2, ca2)
    beginningProfit = profitA1 + profitA2
    print('\nYour beginning average profit per person for A1 and A2 is: $' + str(round(beginningProfit/trials,2)) +'\n')

    totalProfit = beginningProfit

    locationSteps = []
    for i in range(0,21):
        locationSteps.append(i/2)

    cashSteps = []
    for i in range(8,25):
        cashSteps.append(i/4)

    for x in cashSteps:
        for y in cashSteps:
            profitA1, profitA2 = cafeshop(trials, la1, x, la2, y)
            currentTotalProfit = profitA1 + profitA2
            if(currentTotalProfit > totalProfit):
                totalProfit = currentTotalProfit
                ca1 = x
                ca2 = y
                print('C(A1): ' + str(x), 'C(A2): ' + str(y), 'Current TAPPP: $' + str(round(totalProfit/trials,2)))

    print('\nC(A1): ' + str(ca1), 'C(A2): ' + str(ca2), 'Current TAPPP: $' + str(round(totalProfit/trials,2)) + '\n')

    for i in locationSteps:
        for j in locationSteps:
            profitA1, profitA2 = cafeshop(trials, i, ca1, j, ca2)
            currentTotalProfit = profitA1 + profitA2
            if(currentTotalProfit > totalProfit):
                totalProfit = currentTotalProfit
                la1 = i
                la2 = j
                print('L(A1): ' + str(i), 'L(A2): ' + str(j), 'Current TAPPP: $' + str(round(totalProfit/trials,2)))
    print('\nL(A1): ' + str(la1), 'L(A2): ' + str(la2), 'Current TAPPP: $' + str(round(totalProfit/trials,2)) + '\n')

    print('L(A1): ' + str(la1), 'C(A1): $' + str(ca1), 'L(A2): ' + str(la2), 'C(A2): $' + str(ca2))
    print('Final Profit per person: $' + str(round(totalProfit/trials,2)))
    print('Change in total profit per person: $' + str(round((totalProfit-beginningProfit)/trials,2)) + '\n')

if __name__=="__main__":
    optimizer()