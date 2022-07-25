## P
# M*N
# 8*8 체스판으로
# 검 흰 번갈아
# 다시 칠해야 하는 정사각형의 갯수를 구하시오

## I
# N, M (8~50)
# B 검은색 W 흰색
# 뒤에는 행렬

## O
# 다시 칠해야 하는 정사각형 갯수의 최솟값

from sys import stdin, stdout
from itertools import cycle
input = lambda: stdin.readline().rstrip()
print = lambda x : stdout.write(str(x))

def solution(N: int, M: int, matrix: list):
  res: int = 65
  cycC: cycle = cycle( ['B', 'W'] )
  row1: list = [cycC.__next__() for _ in range(8)]; cycC.__next__()
  row2: list = [cycC.__next__() for _ in range(8)]

  cycR: cycle = cycle([row1, row2])
  boardB: list = [cycR.__next__() for _ in range(8)]; cycR.__next__()
  boardW: list = [cycR.__next__() for _ in range(8)]

  for mR in range(N - 7):
    for mC in range(M - 7):
      cntB: int = 0
      cntW: int = 0
      for r in range(8):
        for c in range(8):
          if ( matrix[mR + r][mC + c] != boardB[r][c] ):
            cntB += 1
          if ( matrix[mR + r][mC + c] != boardW[r][c] ):
            cntW += 1
      res = min(res, cntB)
      res = min(res, cntW)
  print(res)

if __name__ == "__main__":
  N, M = map(int, input().split())
  matrix: list = [list(input()) for _ in range(N)]
  solution(N, M, matrix)
