def split_in_two(ns):
    return (ns[0:int(len(ns)//2)], ns[int(len(ns)//2):])

def mergesort(left, right):
    left = left.sorted()
    right = right.sorted()

    if left[0] < right[0]:
        return left.extend(right)
    else:
        return right.extend(right)

