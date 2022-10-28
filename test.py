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



def recurse_tree(data, x):
    key = x[0]
    val = x[1]
    if key in data:
        data[key][val] = {}
        return True
    if not len(data):
        return
    for _,instance in data.items():
        if len(instance):
            boolRes = recurse_tree(instance, x) 
            if boolRes:
                return
        

def to_tree(source):
    resultTree = {}
    for x in source:
        if not x[0]:
            resultTree[x[1]] = {}
        recurse_tree(resultTree, x)
    return resultTree
    

assert to_tree(source) == expected