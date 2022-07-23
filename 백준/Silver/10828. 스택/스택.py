import sys
input = sys.stdin.readline
n = int(input())

class Stack:
  def __init__(self):
    self.list = []
  def push(self, el):
    self.list.append(el)
  def pop(self):
    if self.list == []:
      return -1
    else:
      return self.list.pop()
  def empty(self):
    if self.list == []:
      return 1
    else:
      return 0
  def size(self):
    return len(self.list)
  def top(self):
    if self.list == []:
      return -1
    else:
      return self.list[len(self.list) - 1]

stack = Stack()
for i in range(n):
  cmd = input().split()
  ops = cmd[0]
  if (ops == "push"):
    stack.push(cmd[1])
  elif (ops == "pop"):
    print(stack.pop())
  elif (ops == "empty"):
    print(stack.empty())
  elif (ops == "top"):
    print(stack.top())
  elif (ops == "size"):
    print(stack.size())