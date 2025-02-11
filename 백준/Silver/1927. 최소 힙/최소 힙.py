import heapq, sys

input = sys.stdin.readline
N = int(input())

lst = [int(input()) for _ in range(N)]
# print(lst)
a = []
for i in range(N):
    if lst[i] == 0:
        if a:
            b = heapq.heappop(a)
            print(b)
        else:
            print(0)
    else:
        heapq.heappush(a,lst[i])