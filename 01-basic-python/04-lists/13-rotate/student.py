# Write your code here
"""
def rotate(xs, n):
    xs[:] = xs[n:] + xs[:n]
"""

def rotate(xs, n = 0):
    for i in enumerate(xs.copy()):
        xs[i[0] - n] = i[1]
    #print(xs)
    
rotate([1, 2, 3, 4, 5], 4)