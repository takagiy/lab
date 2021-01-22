def flipvx(n, v):
    return (n - v) % n

def fliptree(tree):
    n = len(tree)
    flipped = [None] * n 
    for v in range(n):
        flipped[flipvx(n, v)] = list(map(lambda u: flipvx(n, u), tree[v]))
    return flipped
