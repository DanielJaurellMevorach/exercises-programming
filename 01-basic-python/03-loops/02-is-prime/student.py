# Write your code here
def is_prime(n):
    
    counter = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
            
    if counter == 2:
        return True
    else:
        return False
        
print(is_prime(4))