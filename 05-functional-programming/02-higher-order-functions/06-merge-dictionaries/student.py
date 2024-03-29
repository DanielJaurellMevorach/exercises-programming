def merge_dictionaries(d1, d2, merge_function):
    unique = dict()
    for key, value in d1.items():
        if value not in [value for key, value in d2.items()]:
            unique[key] = value
            
    for key, value in d2.items():
        if value not in [value for key, value in d1.items()]:
            unique[key] = value
            
    for key, value in d2.items():
        if value in [value for key, value in d1.items()]:
            unique[key] = merge_function(unique[key], sum([key for key, value in d1.items() if value == d2[key]]), value)
            
    return unique
            
    