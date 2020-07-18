def _load_dict(weights, limit):
    temp = {}

    for i, w in enumerate(weights):
        if w <= limit:
            if w in temp:
                temp[w] += [i]
            else:
                temp[w] = [i]

    return temp


def _expand_pairs(pairs):
    def _flatten_combine(r, l):
        temp = []
        for item in r:
            temp.append((item, l[0]))
        return temp

    
    expanded = []

    for pair in pairs:
        if len(pair[0]) > 1:
            expanded += _flatten_combine(pair[0], pair[1])
        elif len(pair[1]) > 1:
            expanded += _flatten_combine(pair[1], pair[0])
        else:
            expanded.append(
                tuple([pair[0][0], pair[1][0]])
                )
    return expanded



def _order_pairs_by_weight(pairs, weights):
    def _order_pair(pair, weights):
        i1, i2 = pair
        if weights[i1] > weights[i2]:
            return pair 
        return (i2, i1)

    temp = []
    for pair in pairs:
        temp.append(_order_pair(pair, weights))
    
    return temp

def _order_pairs_by_index(pairs):
    temp = []
    
    for pair in pairs:
        i1, i2 = pair
        if pair[0] > pair[1]:
            return pair
    return (i2, i1)


def _remove_repeats(pairs):
    temp = {}
    [temp.update({pair:0}) for pair in pairs]
    return list(temp.keys())


def get_indices_of_item_weights(weights, length, limit):
    # Create lookup dictionary
    lookup = _load_dict(weights, limit)

    # Get valid pairs
    pairs = []
    for w in list(lookup.keys()):
        if limit-w in lookup:
            pairs.append(
                (lookup[w], lookup[limit-w])
            )

    if len(pairs) < 1:
        return None

    return _remove_repeats(
                _order_pairs_by_index(
                    _expand_pairs(pairs),
        ))



if __name__ == "__main__": 
    weights_3 = [4, 4, 6, 10, 15, 16]
    answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
    print(answer_3)
