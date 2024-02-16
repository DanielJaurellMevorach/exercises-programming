# Write your code here
def last_digit(n):
    return int(str(n)[-1])

def remove_last_digit(n):
    if len(str(n)) > 1:
        return int(str(n)[:-1])
    else:
        return 0

def digit_sum(n):
    
    print(f"last digit: {last_digit(n)}")
    print(f"without last digit: {remove_last_digit(n)}")
    
    total = last_digit(n)
    
    if len(str(n)) > 1:
        
        for digit in str(remove_last_digit(n)):
            total += int(digit)
        
    return total

print(digit_sum(1))