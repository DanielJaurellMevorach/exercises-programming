"""
def take_while(xs, condition):
    return ([element for element in xs[:xs.index(condition(element) == False)]], [element for element in xs[xs.index(condition(element) == False):]])
"""
"""
def take_while(xs, condition):
    elements_before = [element for element in xs if condition(element)]
    elements_after = [element for element in xs[xs.index(condition(element) == False):]]
    return (elements_before, elements_after)
"""

def take_while(xs, condition):
    falsy = None
    for element in xs:
        if not condition(element):
            falsy = element
            break
    if falsy is None:
        return (xs, [])
    else:
        falsy_index = xs.index(falsy)
        return (xs[:falsy_index], xs[falsy_index:])