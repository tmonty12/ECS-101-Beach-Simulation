import random
from part3 import cafeshop

def optimizer():
    # Has the user input costs and locations for A1 and A2 (should not really matter in the end)
    la1 = eval(input("Enter the location of A1: "))
    ca1 = eval(input("Enter the price of one cup of coffee at A1: "))
    la2 = eval(input("Enter the location of A2: "))
    ca2 = eval(input("Enter the price of one cup of coffee at A2: "))
    # Only run 100,000 trials - 1,000,000 would take too much time and not gain relevant accuracy
    trials = 100000

    # Calculate the beginning profit using the program from part 3
    profitA1, profitA2 = cafeshop(trials, la1, ca1, la2, ca2)
    beginningProfit = profitA1 + profitA2
    print('\nYour beginning average profit per person for A1 and A2 is: $' + str(round(beginningProfit/trials,2)) +'\n')

    # Store the beginning profit in totalProfit, this variable will be used to determine
    # if a possible combination yields a greater profit
    totalProfit = beginningProfit

    # Creates a list of locations to loop through and simulate
    locationSteps = [] #[0,0.5,1,1.5,2 ...10]
    for i in range(0,21):
        locationSteps.append(i/2)

    # Creates a list of costs to loop through and simulate
    costSteps = [] # [2,2.25,2.5 ...6]
    for i in range(8,25):
        costSteps.append(i/4)

    # Double for loop goes through every possible cost combination for A1 and A2 given the costSteps
    # while holding the location variables fixed
    for x in costSteps:
        for y in costSteps:
            # Calculate the profit of costs x = ca1 and y = ca2
            profitA1, profitA2 = cafeshop(trials, la1, x, la2, y)
            currentTotalProfit = profitA1 + profitA2
            # Determine if the current cost combination yields a greater profit
            if(currentTotalProfit > totalProfit):
                # If so the new max profit will be stored in totalProfit, and the new costs of A1 and A2 are stored
                totalProfit = currentTotalProfit
                ca1 = x
                ca2 = y
                print('C(A1): ' + str(x), 'C(A2): ' + str(y), 'Current TAPPP: $' + str(round(totalProfit/trials,2)))

    # This print statement occurs after the cost has been optimized
    print('\nC(A1): ' + str(ca1), 'C(A2): ' + str(ca2), 'Current TAPPP: $' + str(round(totalProfit/trials,2)) + '\n')

    # Same logic as with the previous double loop except now we are optimizing the locations of A1 and A2
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

    # These print statements output the best combinations of cost and location for A1 and A2, show the final profit per person
    # and show the change in total profit per person from the beginning to the end
    print('L(A1): ' + str(la1), 'C(A1): $' + str(ca1), 'L(A2): ' + str(la2), 'C(A2): $' + str(ca2))
    print('Final Profit per person: $' + str(round(totalProfit/trials,2)))
    print('Change in total profit per person: $' + str(round((totalProfit-beginningProfit)/trials,2)) + '\n')

if __name__=="__main__":
    optimizer()
