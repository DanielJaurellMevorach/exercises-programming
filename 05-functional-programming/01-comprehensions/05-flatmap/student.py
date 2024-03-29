def genres(movies):
    return {movie.genres for movie in movies}

def actors(movies):
    return {movie.actors for movie in movies}

def repeat_consecutive(xs, n):
    return [element for element in xs for x in range(n)]

def repeat_alternating(xs, n):
    return [element for element in range(n) for _ in xs]