import sys
input = lambda: sys.stdin.readline()

class Oven:
  def __init__(self, hour, min):
    self.hour = hour
    self.min = min

  def hAdd(self, hour):
    self.hour += hour
    if (self.hour >= 24):
      self.hour = self.hour % 24
  def mAdd(self, min):
    self.min += min
    if (self.min >= 60):
      self.hAdd(self.min // 60)
      self.min = self.min % 60
  def show(self):
    return print(f'{self.hour} {self.min}')

now = [*map(int, input().split())]

aux = int(input())
oven = Oven(now[0], now[1])

oven.mAdd(aux)
oven.show()