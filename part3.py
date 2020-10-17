import random



def cafeshop(LA1, CA1, LA2, CA2):
    i = 0
    profitA1=0
    profitA2=0
    LB1=4
    CB1=5
    LB2=8
    CB2=5
    while i < 1000001:
        buyer = random.randint(0, 10)
        print(buyer)

        scoreA1 = (10 - abs(buyer - LA1)) + 3 * (6 - CA1)
        scoreA2 = (10 - abs(buyer - LA2)) + 3 * (6 - CA2)
        scoreB1 = (10 - abs(buyer - LB1)) + 3 * (6 - CB1)
        scoreB2 = (10 - abs(buyer - LB2)) + 3 * (6 - CB2)

        totalScore=scoreA1+scoreA2+scoreB1+scoreB2
        PA1 = scoreA1 + totalScore
        PA2 = scoreA2 + totalScore
        PB1 = scoreB1 + totalScore
        PB2 = scoreB2 + totalScore

        if PA1 > PB1 and PA2 > PB2:
            profitA1 = profitA1 + (CA1 - 2)
        elif PA2 > PB1 and PA2 > PB2:
            profitA2 = profitA2 + (CA2 - 2)
        i=i+1

    #PPP=profit per person
    AvgPPPA1=profitA1/i
    AvgPPPA2=profitA2/i

    print(AvgPPPA1)
    print(AvgPPPA2)

if __name__=="__main__":

    LA1 = eval(input("enter the location of A1: "))
    CA1 = eval(input("enter the price of one cup of coffee in A1: "))

    LA2 = eval(input("enter the location of A2: "))
    CA2 = eval(input("enter the price of one cup of coffee in A2: "))

    cafeshop(LA1,CA1,LA2,CA2)