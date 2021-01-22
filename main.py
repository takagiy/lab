ist0 = [
# 0 ->
  [1],
# 1 ->
  [2, 5, 9, 13, 17],
# 2 ->
  [3, 6, 10, 14, 18],
# 3 ->
  [4, 7, 11, 15, 19],
# 4 ->
  [12],
# 5 ->
  [],
# 6 ->
  [],
# 7 ->
  [8],
# 8 ->
  [],
# 9 ->
  [],
# 10 ->
  [],
# 11 ->
  [],
# 12 ->
  [],
# 13 ->
  [],
# 14 ->
  [],
# 15 ->
  [16],
# 16 ->
  [],
# 17 ->
  [],
# 18 ->
  [],
# 19 ->
  [],
]

ist1 = [
# 0 ->
  [4],
# 1 ->
  [],
# 2 ->
  [1],
# 3 ->
  [2],
# 4 ->
  [3, 5, 8, 16],
# 5 ->
  [6, 9, 13, 17],
# 6 ->
  [7, 10, 14, 18],
# 7 ->
  [11, 15, 19],
# 8 ->
  [],
# 9 ->
  [],
# 10 ->
  [],
# 11 ->
  [12],
# 12 ->
  [],
# 13 ->
  [],
# 14 ->
  [],
# 15 ->
  [],
# 16 ->
  [],
# 17 ->
  [],
# 18 ->
  [],
# 19 ->
  [],
]

ist2 = [
# 0 ->
  [8],
# 1 ->
  [],
# 2 ->
  [],
# 3 ->
  [],
# 4 ->
  [],
# 5 ->
  [1],
# 6 ->
  [2, 5],
# 7 ->
  [3, 6],
# 8 ->
  [4, 7, 9, 12, 16],
# 9 ->
  [10, 13, 17],
# 10 ->
  [11, 14, 18],
# 11 ->
  [15, 19],
# 12 ->
  [],
# 13 ->
  [],
# 14 ->
  [],
# 15 ->
  [],
# 16 ->
  [],
# 17 ->
  [],
# 18 ->
  [],
# 19 ->
  [],
]

def flipvx(v):
    return (20 - v) % 20

def fliptree(tree):
    flipped = [None] * 20 
    for v in range(20):
        flipped[flipvx(v)] = list(map(flipvx, tree[v]))
    return flipped

def isspanning(tree, startv = 0, visited = None):
    if visited == None:
        visited = [startv]
    for neighbor in tree[startv]:
        visited.append(neighbor)
        isspanning(tree, startv = neighbor, visited = visited)
    expected = list(range(20))
    return sorted(visited) == expected

def isindependent(tree):


ists = [
  ist0, ist1, ist2,
  fliptree(ist0), fliptree(ist1), fliptree(ist2)
]

def main():
    for i in range(6):
        print('Is IST_{} spanning? : {}'.format(i, isspanning(ists[i])))

if __name__ == '__main__':
    main()
