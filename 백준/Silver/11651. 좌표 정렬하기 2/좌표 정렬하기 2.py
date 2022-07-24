## prob
# 2차원 점 n
# 1. y좌표 오름차순
# 2. y같으면 x좌표 오름차순

## input
# n (1 ~ 100k)
#  Xi, Yi (-100k, 100k)

import sys
input = lambda: sys.stdin.readline()

n = int(input())
matrix = []
for i in range(n):
  x, y = map(int, input().split())
  matrix.append([x, y])

res = sorted(matrix ,key = lambda cor: (cor[1], cor[0]))

for c in res:
  print(c[0], c[1])