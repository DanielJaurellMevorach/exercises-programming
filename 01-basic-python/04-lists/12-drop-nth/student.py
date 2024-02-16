# Write your code here

def drop_nth(xs, n):
    return [xs[element] for element in range(len(xs)) if element != n]