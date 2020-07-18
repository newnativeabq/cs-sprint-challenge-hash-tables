def _is_pos(x):
    return x > 0

def _is_neg(x):
    return x < 0



def has_negatives(a):
    lookup = {}

    found = []
    lost = []

    for item in a:
        if _is_neg(item):
            lookup[item] = 0

        elif _is_pos(item):
            if item*(-1) in lookup.keys():
                found.append(item)
            else:
                lost.append(item)
    
    for item in lost:
        if item*(-1) in lookup.keys():
            found.append(item)

    return found


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
