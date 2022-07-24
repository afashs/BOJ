from sys import stdin, stdout
from itertools import combinations
input = lambda: stdin.readline()
print = lambda o: stdout.write(str(o))

def solution(N: int, M: int, li: list):
  res: int = 0
  for triple in combinations(li, 3):
    sumT = sum(triple)
    if (sumT > M):
      continue
    elif (sumT > res):
      res = sumT
    else:
      continue
  print(res)

if (__name__ == "__main__") :
  N, M = map(int, input().split())
  li = list(map(int, input().split()))
  solution(N, M, li)
