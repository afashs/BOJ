## P
# 자연수 N 의 분해합은 N + 자리수의 합
# M의 분해합이 N이면 M은 N의 생성자
# N이 주어졌을때 가장 작은 생성자를 구하는 프로그램

## I
# N (1 ~ 1m)

from sys import stdin, stdout
from itertools import permutations
input = lambda: stdin.readline().rstrip()
print = lambda x: stdout.write(str(x))

def solution(N: str):
  M: int = int(N)
  for i in range(M):
    sumP = sum([int(j) for j in str(i)])
    if ( i + sumP == M):
      print(i)
      break
  else:
    print(0)

if __name__ == "__main__":
  N = input()
  solution(N)