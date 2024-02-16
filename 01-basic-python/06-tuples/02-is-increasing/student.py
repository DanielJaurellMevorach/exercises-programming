# Write your code here
"""
def is_increasing(ns):
    ms = [ns[i] for i in range(len(ns)) if i > 0]
    ms = list(zip(ns, ms))
    for i in ms:
        print(i)
        for j in range(len(i)):
            print(i[j] , i[-1])
            if i[j] <= i[-1]:
                return True 
    return False
"""

def is_increasing(ns):
    for i in range(len(ns) - 1):
        if ns[i] >= ns[i + 1]:
            return False
    return True

print(is_increasing([1, 2]))
