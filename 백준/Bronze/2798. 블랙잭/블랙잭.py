## P
# 21 이하
# N장 중에서 3장
# M <= 최대한 가깝게

## I
# N (3 ~ 100) M (10 ~ 300k)
# list

from sys import stdin, stdout
from itertools import combinations
input = lambda: stdin.readline()
print = lambda o: stdout.write(str(o))
res: list = []

def solution(N: int, M: int, li: list):
  for triple in combinations(li, 3):
    if (sum(triple) > M):
      continue
    else:
      res.append(sum(triple))
  print(max(res))

if (__name__ == "__main__") :
  N, M = map(int, input().split())
  li = list(map(int, input().split()))
  solution(N, M, li)
