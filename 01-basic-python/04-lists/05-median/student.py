# Write your code here
def median(ns):
    ns  = sorted(ns.copy())
    print(ns)
    if len(ns) == 1:
        return ns[0]
    elif len(ns) % 2 != 0:
        return ns[int(len(ns) / 2)]
    else:
        return (ns[int(len(ns) / 2)] + ns[int(len(ns) / 2) - 1]) / 2

print(median([4, 2, 6, 5, 4, 1, 2, 7, 6, 4, 5, 9]))