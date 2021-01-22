def flipvx(v):
    return (20 - v) % 20

def fliptree(tree):
    flipped = [None] * 20 
    for v in range(20):
        flipped[flipvx(v)] = list(map(flipvx, tree[v]))
    return flipped
