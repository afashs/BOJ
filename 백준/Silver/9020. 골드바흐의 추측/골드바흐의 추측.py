## P
# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다
# 이것의 두 소스를 표현한 것을 골드바흐 파티션이라고 부름
# 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력

import sys
input = lambda: sys.stdin.readline()

def isPrime(n):
  if n == 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

n = int(input())

for _ in range(n):
  num = int(input())
  a, b = num // 2, num // 2
  while a > 0:
    if isPrime(a) and isPrime(b):
      print(a, b)
      break
    else:
      a -= 1
      b += 1
