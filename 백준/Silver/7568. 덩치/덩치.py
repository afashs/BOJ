from sys import stdin, stdout
input = lambda: stdin.readline()
print = lambda x : stdout.write(str(x))

res: list = []

def solution(li:list):
  for w, h in li:
    rank: int = 1
    for _w, _h in li:
      if _w > w and _h > h:
        rank += 1
    res.append(str(rank))
  print(' '.join(res))

if __name__ == "__main__":
  N: int = int(input())
  li: list = [list(map(int, input().split())) for _ in range(N)]
  solution(li)