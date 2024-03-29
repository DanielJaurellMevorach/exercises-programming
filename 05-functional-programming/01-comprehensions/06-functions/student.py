def movie_count(movies, director):
    return len([x for x in movies if director in x.director])

def longest_movie_runtime_with_actor(movies, actor):
    return max([x.runtime for x in movies if actor in x.actors])

def has_director_made_genre(movies, director, genre):
    return any([x.genres for x in movies if director in x.director and genre in x.genres])

