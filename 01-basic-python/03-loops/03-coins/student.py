# Write your code here

def coins(one, two, five, goal):
    for i in range(goal // one + 1):
        for j in range(goal // two + 1):
            for k in range(goal // five + 1):
                if (i * one) + (j * two) + (k * five) == goal:
                    return True
    return False
    
    