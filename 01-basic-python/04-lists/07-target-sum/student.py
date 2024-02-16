# Write your code here

from itertools import permutations 

#target_sum([1, 2, 3], 5)

# Get all permutations of length 2 
# and length 2 
#perm = permutations([1, 2, 3], 2) 

"""def target_sum(ns):
    for i in range(len(ns)):
        for elements in ns[0:i]:
            perm = list(permutations([elements], int(len(str(elements)))))
            print(perm)
            
target_sum([1, 2, 3])"""

def target_sum(ns, target):
    for i in range(len(ns)):
        for j in range(i, len(ns)):
            if ns[i] + ns[j] == target:
                return True
    return False