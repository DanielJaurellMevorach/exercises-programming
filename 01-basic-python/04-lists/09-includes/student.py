# Write your code here

def includes(xs, ys):
    if len(ys) == 0 and len(xs) == 0:
        return True
    else:
        for element in ys:
            print(element)
            if element in xs:
                return True
        return False

print(includes([2], []))