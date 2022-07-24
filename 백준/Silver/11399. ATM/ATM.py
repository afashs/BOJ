## prob
#  atm 1대
# n 명 각각 i
# Pi 분 씩 소요

## input
# 사람 수 n
# Pi list

import sys
input = lambda: sys.stdin.readline()

n = int(input())
li = [*map(int, input().split())]
res = 0

sLi = sorted(li)

for i in range(1, 1 + n):
  res += sum(sLi[:i])

print(res)