## P
# s = (r1 + r2) / 2
# 2s = r1 + r2
# 2s - r1 = r2

## in
# R1 , S

## out
# r2

import sys
input = lambda: sys.stdin.readline()

class Calc:
  def __init__(self, r1, s):
    return print(2 * s - r1)

r1, s = map(int, input().split())
Calc(r1, s)