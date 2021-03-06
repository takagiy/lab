N = 31
D1 = 4
D2 = 8

ist0 = [
# 0 ->
  [1],
# 1 ->
  [2, 5, 9, 24, 28],
# 2 ->
  [3, 6, 10, 25, 29],
# 3 ->
  [4, 7, 11, 26, 30],
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
  [13, 16],
# 13 ->
  [14, 17],
# 14 ->
  [18],
# 15 ->
  [],
# 16 ->
  [],
# 17 ->
  [],
# 18 ->
  [],
# 19 ->
  [20, 23],
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
  [27],
# 27 ->
  [],
# 28 ->
  [],
# 29 ->
  [],
# 30 ->
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
  [3, 5, 8, 12, 27],
# 5 ->
  [6, 9, 13, 28],
# 6 ->
  [7, 10, 14, 29],
# 7 ->
  [11, 15, 30],
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
  [16, 19, 23],
# 16 ->
  [17, 20, 24],
# 17 ->
  [18, 21, 25],
# 18 ->
  [22, 26],
# 19 ->
  [],
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
# 30 ->
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
  [20],
# 13 ->
  [21],
# 14 ->
  [15, 22],
# 15 ->
  [],
# 16 ->
  [],
# 17 ->
  [],
# 18 ->
  [19],
# 19 ->
  [27],
# 20 ->
  [24, 28],
# 21 ->
  [25, 29],
# 22 ->
  [23, 26, 30],
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
# 30 ->
  [],
]

from ctorutil import *

ists = [
  ist0, ist1, ist2,
  fliptree(ist0), fliptree(ist1), fliptree(ist2)
]
