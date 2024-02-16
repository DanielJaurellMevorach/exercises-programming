# Write your code here

def add_indices(xs):
    new_xs = []
    for index, element in enumerate(xs):
        new_xs.append((index, element))
    
    return new_xs
print(add_indices(['a', 'b', 'c']))

""""

return [(counter, line) for counter, line in enumerate(xs)]

"""
        