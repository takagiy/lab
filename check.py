def isspanning(tree, startv = 0, visited = None):
    if visited == None:
        visited = [startv]
    for neighbor in tree[startv]:
        visited.append(neighbor)
        isspanning(tree, startv = neighbor, visited = visited)
    expected = list(range(20))
    return sorted(visited) == expected

def isindependent(ists):
    result = True
    anceses = [None] * 6
    for i in range(6):
        anceses[i] = collectances(ists[i])
    for v in range(1, 20):
        for ti in range(6):
            for tj in range(ti + 1, 6):
                commonances = set(anceses[ti][v]) & set(anceses[tj][v])
                if commonances != {0}:
                    print('ERRROR: NOT INDEPENDENT BECAUSE OF VERTEX {}!!'.format(v))
                    print('NOTE:   Common ancestors for vertex {} in IST_{} and IST_{} : {}'.format(v, ti, tj, commonances))
                    result = False
    return result

def collectances(tree, parent = 0, ances = None):
    if ances == None:
        ances = [[]] * 20
    for neighbor in tree[parent]:
        ances[neighbor] = ances[parent] + [parent]
        collectances(tree, parent = neighbor, ances = ances)
    return ances

def main():
    from istset0 import ists

    for ti in range(6):
        ances = collectances(ists[ti])
        for vi in range(20):
            print('Ancestors of vertex {} in IST_{} : {}'.format(vi, ti, ances[vi]))
    for i in range(6):
        print('Is IST_{} spanning? : {}'.format(i, isspanning(ists[i])))
    print('Is all ISTs independent? : {}'.format(isindependent(ists)))

if __name__ == '__main__':
    main()
