def tree(N, tree):
    result = '\\begin{tikzpicture}\n'
    result += '  \\xcrCR[xcr radius=3]({})[\n'.format(N)
    for u in range(len(tree)):
        if tree[u]:
            result += '    {} adj '.format(u)
            result += ' '.join(map(str,tree[u]))
            result += ',\n'
    result += '  ]\n'
    result += '\\end{tikzpicture}\n'
    return result

def treeset(N, ists):
    result = '\\documentclass{article}\n'
    result += '\\usepackage{geometry}\n'
    result += '\\geometry{left=0in, right=0in, top=1in, bottom=0in}\n'
    result += '\\usepackage{tikz}\n'
    result += '\\usepackage{extchordalring}\n'
    result += '\\begin{document}\n'
    result += '\\begin{center}'
    for i in range(3):
        result += tree(N, ists[i])
        result += '\\hspace{3cm}'
        result += tree(N, ists[i + 3])
        if i < 2:
            result += '\n'
            result += '\\vspace{1cm}\n'
            result += '\n'
    result += '\\end{center}'
    result += '\\end{document}'
    return result

def save(path, N, ists):
    with open(path, 'w') as f:
        f.write(treeset(N, ists))

def compile(path, N, ists):
    import os
    save(path, N, ists)
    os.system(f'lualatex {path}')

