## P
# 장부 관리 재민이
# 재현이가 재민이 보조
# 재현이가 잘못 부름
# 잘못부르면 0 을 외쳐서 지우기
# 마지막에 sum

## i
# k (1 ~ 1m)
# 0일때는 지우기
# 0일때는 empty 상태가 아님 보장
# sum (2^31 - 1)

## s
# k 번 반복
# 큐에 넣고 마지막에 sum
# 받으면서 바로바로 지우는게 관리가 더 편할듯

# k 번 반복
from sys import stdin, stdout
input = lambda: stdin.readline()
print = lambda x : stdout.write(str(x))

def solution(k: int):
  res: list = []
  for _ in range(k) :
    num = int(input())
    if (num == 0) :
      res.pop()
    else:
      res.append(num)
  print(sum(res))

if __name__ == "__main__":
  k: int = int(input())
  solution(k)