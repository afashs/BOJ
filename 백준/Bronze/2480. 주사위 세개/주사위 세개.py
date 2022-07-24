import sys
from collections import Counter
input = lambda: sys.stdin.readline()

class Calculator:
    def __init__(self, nums):
      self.dict = Counter(nums)
    def judge(self):
      cnts = self.dict.values()
      if(3 in cnts):
        i = next(iter(filter(lambda el: el[1] == 3 , self.dict.items())))
        return 10000 + (i[0] * 1000)
      elif(2 in cnts) :
        i = next(iter(filter(lambda el: el[1] == 2 , self.dict.items())))
        return 1000 + (i[0] * 100)
      else:
        return max(self.dict.keys()) * 100

nums = [*map(int, input().split())]
calc = Calculator(nums)
print(calc.judge())
