def directors(movies):
    return {x.director for x in movies}

def common_elements(xs, ys):
    return {x for x in xs if x in ys}