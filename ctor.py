from ctorutil import *

def makeists(N, D1, D2):
    ist0 = [[] for i in range(N)]
    ist1 = [[] for i in range(N)]
    ist2 = [[] for i in range(N)]

    ist0[0] += [1]

    for v in range(1, D1):
        ist0[v] += [v + 1, v + D1, v + D2, v - D1 + N, v - D2 + N]

    ist0[D2 - 1] += [D2]

    ist0[N - D1 - 1] = [N - D1]

    start = D1 - 1 + D2
    end = 1 - D2 + N

    for i in range(start, end - D2, D2):
        ist0[i] += [i + D2]

    for i in range(start, end - D1, D2):
        ist0[i] += [i + D1]

    for i in range(start, end - 1):
        if (i - start) % D1 != D1 - 1:
            ist0[i] += [i + 1]

    ist1[0] += [D1]

    for i in range(1, D1):
        ist1[i + 1] += [i]

    for i in range(D1, D2 - 1):
        ist1[i] += [i + 1]

    for i in range(D1, D2):
        ist1[i] += [i + D1, i + D2, i - D2 + N]

    start = D1 + D2
    end = D1 - D2 + N

    for i in range(start, end - D2):
        if (i - start) % D2 < D1:
            ist1[i] += [i + D2]

    for i in range(start, end - D1):
        if (i - start) % D2 < D1:
            ist1[i] += [i + D1]

    ist2[0] += [D2]

    start = D2
    end = D1 - D2 + N

    for i in range(N - 1, end - 1, -1):
        ist2[i - D2] += [i]

    for i in range(D1 + 1, D2 + 1):
        ist2[i] += [i - D1]

    for i in range(D1 + 2, D2 + 1):
        ist2[i] += [i - 1]

    for i in range(D2, D2 + D1 - 2):
        ist2[i] += [i + 1]

    for i in range(start, flipvx(N, D2)):
        if (i - start) % D1 == D1 - 2:
            ist2[i] += [i + 1]

    for i in range(start, end - D1):
        if (i - start) % D2 < D1 - 1:
            ist2[i] += [i + D1]

    for i in range(start, end - D2):
        if (i - start) % D2 < D1 - 1:
            ist2[i] += [i + D2]

    for i in range(flipvx(N, D2 - 1), end):
        if (i - start) % D1 == D1 - 1:
            if i not in ist1[i - D1]:
                ist2[i - D1] += [i]
            else:
                ist2[i - D2] += [i]

    ists = [
      ist0, ist1, ist2,
      fliptree(ist0), fliptree(ist1), fliptree(ist2)
    ]

    return ists
