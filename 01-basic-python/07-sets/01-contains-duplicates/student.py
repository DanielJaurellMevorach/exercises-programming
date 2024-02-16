# Write your code here

"""
Write your code here
def contains_duplicates(xs):
    xs_control = []
    for i in xs:
        if i not in xs_control:
            xs_control.append(i)
        else:
            return True
    return False

"""

def contains_duplicates(xs):
    xs_contol = set(xs)
    if len(xs_contol) != len(xs):
        return True
    return False