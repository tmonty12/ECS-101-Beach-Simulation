import random
import time

def cafeshop(T, LA1, CA1, LA2, CA2):
    i = 0
    profitA1=0
    profitA2=0
    LB1=4
    CB1=5
    LB2=8
    CB2=5

    while i <= T:
        customerLocation = random.random()*10

        scoreA1 = (10 - abs(customerLocation - LA1)) + 3 * (6 - CA1)
        scoreA2 = (10 - abs(customerLocation - LA2)) + 3 * (6 - CA2)
        scoreB1 = (10 - abs(customerLocation - LB1)) + 3 * (6 - CB1)
        scoreB2 = (10 - abs(customerLocation - LB2)) + 3 * (6 - CB2)

        totalScore=scoreA1+scoreA2+scoreB1+scoreB2

        PA1 = scoreA1 / totalScore
        PA2 = scoreA2 / totalScore

        randomChoice = random.random()

        if PA1 >= randomChoice:
            profitA1 = profitA1 + (CA1 - 2)
        elif PA1+PA2 >= randomChoice:
            profitA2 = profitA2 + (CA2 - 2)
        i=i+1


    return [profitA1, profitA2]

if __name__=="__main__":
    T = 1000000

    LA1 = eval(input("Enter the location of A1: "))
    CA1 = eval(input("Enter the price of one cup of coffee at A1: "))

    LA2 = eval(input("Enter the location of A2: "))
    CA2 = eval(input("Enter the price of one cup of coffee at A2: "))

    profitA1, profitA2 = cafeshop(T,LA1,CA1,LA2,CA2)

    print("Average profit per person for A1: $" + str(round(profitA1/T,2)))
    print("Average profit per person for A2: $" + str(round(profitA2/T,2)))