import random

def cafeshop(LA1, CA1, LA2, CA2):
    i = 0
    profitA1=0
    profitA2=0
    LB1=4
    CB1=5
    LB2=8
    CB2=5
    trials = 1000000
    while i <= trials:
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

    #PPP=profit per person
    AvgPPPA1=profitA1/trials
    AvgPPPA2=profitA2/trials

    print("Average profit per person of A1: " + str(AvgPPPA1))
    print("Average profit per person of A2: " + str(AvgPPPA2))

if __name__=="__main__":

    LA1 = eval(input("enter the location of A1: "))
    CA1 = eval(input("enter the price of one cup of coffee in A1: "))

    LA2 = eval(input("enter the location of A2: "))
    CA2 = eval(input("enter the price of one cup of coffee in A2: "))

    cafeshop(LA1,CA1,LA2,CA2)