def title_to_director(movies):
    return {x.title:x.director for x in movies}

def director_to_titles(movies):
    return {x.director:[y.title for y in movies if x.director in y.director] for x in movies}