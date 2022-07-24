import sys
_in = lambda: sys.stdin.readline()

def solution(N: int):
    path: list = []

    def hanoi(n: int, src: int, mid: int, dst: int):
        if n == 1:
            path.append(f"{src} {dst}")
        else:
            hanoi(n - 1, src, dst, mid)
            path.append(f"{src} {dst}")
            hanoi(n - 1, mid, src, dst)

    hanoi(N, 1, 2, 3)
    print(len(path))
    print('\n'.join(path))

if __name__ == '__main__':
    N: int = int(_in())
    solution(N)