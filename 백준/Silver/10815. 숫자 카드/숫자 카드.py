## Problem
# 정수 m개
# 카드 n개
# 가지고 있는지 여부 리스트를 알고싶다

## In
# n (1 ~ 500K)
# nli (-10m ~ 10m)
# m (1 ~ 500K)
# mli (-10m ~ 10m)

## Out
# list<true 1 or false 0>

## Solve

import sys
input  = lambda: sys.stdin.readline()

def bSearch(el, nli, st, end):
  while st <= end:
    mid = (st + end) // 2
    if nli[mid] == el:
      return True
    elif nli[mid] > el:
      end = mid - 1
    else:
      st = mid + 1
  return False


n = int(input())
nli = [*map(int, input().split())]
m = int(input())
mli = [*map(int, input().split())]
res = []

snli = sorted(nli)

for el in mli:
  st = 0
  end = len(nli) - 1
  if (bSearch(el, snli, st, end) == True):
    res.append(1)
  else:
    res.append(0)

print(*res)