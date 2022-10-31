source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

def to_tree(source):
    result = {}
    for i in range(len(source)):
        current_turple = source[i]
        string_key = current_turple[0]
        string_val = current_turple[1]
        level = len(string_val)

        ref = result
        for j in range(level):
            keyStart = string_val[:j]
            if j == 0:
                keyStart = None
            keyOffset = string_val
            if j == level - 1:
                if string_key in ref:
                    ref[string_key].update({keyOffset:{}})
                else:
                    ref[string_key] = {keyOffset:{}}
            ref = ref[keyStart]
    result = result[None]
    return result

assert to_tree(source) == expected