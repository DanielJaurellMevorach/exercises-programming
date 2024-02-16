# Write your code here
def contains_duplicates(xs):
    xs_control = []
    for i in xs:
        if i not in xs_control:
            xs_control.append(i)
        else:
            return True
    return False