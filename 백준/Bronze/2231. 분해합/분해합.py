from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda x: stdout.write(str(x))

def solution(N: int):
  minM: int = N - (len(str(N)) * 9)
  for i in range(minM, N):
    sumM: int = sum([int(j) for j in str((i > 0) and i or 0)])
    if ( i + sumM == N):
      print(i)
      break
  else:
    print(0)

if __name__ == "__main__":
  N: int = int(input())
  solution(N)