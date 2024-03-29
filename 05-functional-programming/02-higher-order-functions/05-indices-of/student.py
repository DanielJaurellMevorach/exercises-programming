def indices_of(xs, condition):
    return [element[0] for element in enumerate(xs) if condition(element[1])]