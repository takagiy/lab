from ctorutil import *

N = 31
D1 = 4
D2 = 8

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

ist2[0] += [8]

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

for i in range(flipvx(N, 7), end):
    if (i - start) % D1 == D1 - 1:
        ist2[i - D1] += [i]

#ist2 = [
## 0 ->
#  [8],
## 1 ->
#  [],
## 2 ->
#  [],
## 3 ->
#  [],
## 4 ->
#  [],
## 5 ->
#  [1],
## 6 ->
#  [2, 5],
## 7 ->
#  [3, 6],
## 8 ->
#  [4, 7, 9, 12, 16],
## 9 ->
#  [10, 13, 17],
## 10 ->
#  [11, 14, 18],
## 11 ->
#  [],
## 12 ->
#  [],
## 13 ->
#  [],
## 14 ->
#  [15],
## 15 ->
#  [],
## 16 ->
#  [20, 24],
## 17 ->
#  [21, 25],
## 18 ->
#  [19, 22],
## 19 ->
#  [23],
## 20 ->
#  [],
## 21 ->
#  [],
## 22 ->
#  [],
## 23 ->
#  [],
## 24 ->
#  [],
## 25 ->
#  [],
## 26 ->
#  [],
## 27 ->
#  [],
## 28 ->
#  [],
## 29 ->
#  [],
#]

ists = [
  ist0, ist1, ist2,
  fliptree(ist0), fliptree(ist1), fliptree(ist2)
]
