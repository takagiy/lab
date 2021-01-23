def isspanning(tree, startv = 0, visited = None):
    if visited == None:
        visited = [startv]
    for neighbor in tree[startv]:
        visited.append(neighbor)
        isspanning(tree, startv = neighbor, visited = visited)
    expected = list(range(len(tree)))
    return sorted(visited) == expected

def isindependent(ists):
    result = True
    anceses = [None] * 6
    for i in range(6):
        anceses[i] = collectances(ists[i])
    for v in range(1, len(ists[0])):
        for ti in range(6):
            for tj in range(ti + 1, 6):
                commonances = set(anceses[ti][v]) & set(anceses[tj][v])
                if commonances != {0}:
                    print('ERROR: NOT INDEPENDENT BECAUSE OF VERTEX {}!!'.format(v))
                    print('NOTE:  Common ancestors for vertex {} in IST_{} and IST_{} : {}'.format(v, ti, tj, commonances))
                    result = False
    return result

def collectances(tree, parent = 0, ances = None):
    if ances == None:
        ances = [[]] * len(tree)
    for neighbor in tree[parent]:
        ances[neighbor] = ances[parent] + [parent]
        collectances(tree, parent = neighbor, ances = ances)
    return ances

def countedges(ists):
    count = dict()
    for tree in ists:
        for u in range(len(ists[0])):
            for v in tree[u]:
                if (u, v) in count:
                    count[u, v] += 1
                else:
                    count[u, v] = 1
    return count

def verifynedges(n, d1, d2, count):
    for u in range(n):
        for d in [1, d1, d2, -1, -d1, -d2]:
            v = (u + d) % n
            if v < 0:
                v += n
            if v == 0:
                if (u, v) in count:
                    print('ERROR: Too many edge {} expected zero but found {}'.format((u, v), count[u, v]))
            elif not (u, v) in count:
                print('ERROR: Edge {} expected but not found'.format((u, v)))
            elif count[u, v] != 1:
                print('ERROR: Too many edge {} expected one but found {}'.format((u, v), count[u, v]))

def do_check(N, D1, D2, ists, verbose = False):
    if verbose:
        for ti in range(6):
            ances = collectances(ists[ti])
            for vi in range(len(ists[0])):
                print('Ancestors of vertex {} in IST_{} : {}'.format(vi, ti, ances[vi]))
    for i in range(6):
        print('Is IST_{} spanning? : {}'.format(i, isspanning(ists[i])))
    print('Are all ISTs independent? : {}'.format(isindependent(ists)))
    nedges = countedges(ists)
    verifynedges(N, D1, D2, nedges)

if __name__ == '__main__':
    from istset0 import ists, N, D1, D2
    do_check(N, D1, D2, ists)
