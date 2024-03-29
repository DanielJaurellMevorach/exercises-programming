def title(movies):
    return [x.title for x in movies]

def titles_and_years(movies):
    return [(x.title, x.year) for x in movies]

def titles_and_actor_counts(movies):
    return [(x.title, len(x.actors)) for x in movies]

def reverse_words(sentence):
    return " ".join([word[::-1] for word in sentence.split(' ')])