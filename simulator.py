import random
import time

def beach_simulation(T, LA1, CA1, LA2, CA2):
    i = 0 
    profitA1=0
    profitA2=0
    # Location and Costs for B1 and B2
    LB1=4
    CB1=5
    LB2=8
    CB2=5

    # Loops through T trials
    while i <= T:
        # Randomly generate the customer's location (0-10)
        customerLocation = random.random()*10

        # Calculate the scores for A1, A2, B1, B2
        scoreA1 = (10 - abs(customerLocation - LA1)) + 3 * (6 - CA1)
        scoreA2 = (10 - abs(customerLocation - LA2)) + 3 * (6 - CA2)
        scoreB1 = (10 - abs(customerLocation - LB1)) + 3 * (6 - CB1)
        scoreB2 = (10 - abs(customerLocation - LB2)) + 3 * (6 - CB2)

        # Calculate the total score to use for probability
        totalScore=scoreA1+scoreA2+scoreB1+scoreB2

        # Calculate the probability of a customer choosing A1 and A2
        PA1 = scoreA1 / totalScore
        PA2 = scoreA2 / totalScore

        # Randomly generate the customer's choice
        randomChoice = random.random()

        # If the random choice falls in the range of PA1, add the profit to A1
        if PA1 >= randomChoice:
            profitA1 = profitA1 + (CA1 - 2)
        # If the random choice falls in the range of PA@, add the profit to A2
        elif PA1+PA2 >= randomChoice:
            profitA2 = profitA2 + (CA2 - 2)
        i=i+1

    # Program returns the total profit of A1 and A2 after T trials
    return [profitA1, profitA2]

if __name__=="__main__":
    T = 1000000

    # User inputs the cost and locations for A1 and A2
    LA1 = eval(input("Enter the location of A1: "))
    CA1 = eval(input("Enter the price of one cup of coffee at A1: "))

    LA2 = eval(input("Enter the location of A2: "))
    CA2 = eval(input("Enter the price of one cup of coffee at A2: "))

    # Runs the program on the inputs
    profitA1, profitA2 = cafeshop(T,LA1,CA1,LA2,CA2)

    # Prints the average profit per person for A1 and A1
    print("Average profit per person for A1: $" + str(round(profitA1/T,2)))
    print("Average profit per person for A2: $" + str(round(profitA2/T,2)))