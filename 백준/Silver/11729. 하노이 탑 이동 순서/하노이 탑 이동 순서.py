## P
# 3개의 장대
# n 개의 원판 + 큰순서부터 쌓여있음
# 한번에 한개 + 항상 큰원판이 아래로

## I
# n (1 ~ 20)

## O
# 3번째 장대로 옮긴 횟수 K

import sys
_in = lambda: sys.stdin.readline()

class Tower:
  def __init__(self, disks):
    self.disks = disks
    self.mem = []
    self.polls = [[]] * 3
    self.polls[0] = [i for i in range(self.disks, 0, -1)]
    self.polls[1] = []
    self.polls[2] = []
  def move(self, fromP, toP):
    disk = self.polls[fromP].pop()
    self.polls[toP].append(disk)

def hanoi(tower, n, fromP, toP, auxP):
  if n == 0:
    return
  hanoi(tower, n - 1, fromP, auxP, toP)
  tower.move(fromP, toP)
  tower.mem.append(f"{fromP + 1} {toP + 1}")
  hanoi(tower, n - 1, auxP, toP, fromP)

n = int(_in())
tower = Tower(n)
hanoi(tower, tower.disks, 0, 2, 1)
print(len(tower.mem))
for i in tower.mem:
  print(i)
