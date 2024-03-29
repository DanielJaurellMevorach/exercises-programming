def movies_from_year(movies, year):
    return [x.title for x in movies if x.year == year]

def movies_with_actor(movies, actor):
    return [x.title  for x in movies if actor in x.actors]

def divisors(n):
    return [x for x in range(1, n+1) if n % x == 0]