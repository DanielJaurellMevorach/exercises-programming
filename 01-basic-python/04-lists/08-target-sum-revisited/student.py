# Write your code here
"""
def target_sum(ns, target):
    for i in ns:
        for element in ns:
            if element != i and element + i == target:
                return True
    return False
"""

def target_sum(ns, target):
    for element in range(len(ns)):
        print(element)
        if element < len(ns) - 1:
            if ns[element] != ns[element + 1] and ns[element] != ns[element + 2]:
                if ns[element] + ns[element  + 1] == target:
                    return True
    return False
        
"""
0
1
2
3
""" 

print(target_sum([1, 2, 3, 3], 6))