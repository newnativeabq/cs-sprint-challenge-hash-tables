def _build_keys(array):
    temp = {}
    for val in array:
        temp[val] = 0
    return temp


def _is_in_all_sets(val, keysets):
    test = [val in keys for keys in keysets]
    return sum(test) == len(keysets)


def intersection(arrays):

    # Check for single array
    if len(arrays) == 1:
        return arrays[0]

    # Load check set (doesn't matter which array you seed with)
    keysets = [_build_keys(array) for array in arrays]

    # Check intersection:
    intersection = []
    testarr = arrays[0]
    for val in testarr:
        if _is_in_all_sets(val, keysets):
            intersection.append(val)
        
    return intersection


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
