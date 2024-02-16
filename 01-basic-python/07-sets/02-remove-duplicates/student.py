# Write your code here

"""def remove_duplicates(xs):
    xs_set = set(xs)
    
    if len(xs_set) != len(xs):
        xs.reverse()
        for i in xs:
            if xs.count(i) > 1:
                xs.remove(i)
        xs.reverse()
    return xs
"""

def remove_duplicates(xs):
    seen = set()
    result = []
    for x in xs:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result



print(remove_duplicates([1, 2, 3, 4, 4, 7]))