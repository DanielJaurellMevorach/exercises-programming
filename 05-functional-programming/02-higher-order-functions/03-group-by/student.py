def group_by(xs, key_function):
    return {key: [x for x in xs if key_function(x) == key] for key in set(map(key_function, xs))}