N = 30
D1 = 4
D2 = 8

ist0 = [
# 0 ->
  [1],
# 1 ->
  [2, 5, 9, N - D2 + 1, N - D1 + 1],
# 2 ->
  [3, 6, 10, N - D2 + 2, N - D1 + 2],
# 3 ->
  [4, 7, 11, N - D2 + 3, N - D1 + 3],
# 4 ->
  [],
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
  [12, 15, 19],
# 12 ->
  [13],
# 13 ->
  [14],
# 14 ->
  [],
# 15 ->
  [16],
# 16 ->
  [17],
# 17 ->
  [18],
# 18 ->
  [],
# 19 ->
  [20],
# 20 ->
  [21],
# 21 ->
  [22],
# 22 ->
  [],
# 23 ->
  [],
# 24 ->
  [],
# 25 ->
  [],
# 26 ->
  [],
# 27 ->
  [],
# 28 ->
  [],
# 29 ->
  [],
]

ist0[N - D1 - 1] = [N - D1]

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
  [3, 5, 8, 12, N - D2 + 4],
# 5 ->
  [6, 9, 13, N - D2 + 5],
# 6 ->
  [7, 10, 14, N - D2 + 6],
# 7 ->
  [11, 15, N - D2 + 7],
# 8 ->
  [],
# 9 ->
  [],
# 10 ->
  [],
# 11 ->
  [],
# 12 ->
  [16, 20],
# 13 ->
  [17, 21],
# 14 ->
  [18, 22],
# 15 ->
  [19, 23],
# 16 ->
  [],
# 17 ->
  [],
# 18 ->
  [],
# 19 ->
  [],
# 20 ->
  [24],
# 21 ->
  [25],
# 22 ->
  [],
# 23 ->
  [],
# 24 ->
  [],
# 25 ->
  [],
# 26 ->
  [],
# 27 ->
  [],
# 28 ->
  [],
# 29 ->
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
  [],
# 12 ->
  [],
# 13 ->
  [],
# 14 ->
  [15],
# 15 ->
  [],
# 16 ->
  [20, 24],
# 17 ->
  [21, 25],
# 18 ->
  [19, 22],
# 19 ->
  [23],
# 20 ->
  [],
# 21 ->
  [],
# 22 ->
  [],
# 23 ->
  [],
# 24 ->
  [],
# 25 ->
  [],
# 26 ->
  [],
# 27 ->
  [],
# 28 ->
  [],
# 29 ->
  [],
]

for i in range(1, D1 + 1):
    ist2[N - D2 - i].append(N - i)

from ctorutil import *

ists = [
  ist0, ist1, ist2,
  fliptree(ist0), fliptree(ist1), fliptree(ist2)
]
