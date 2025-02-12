N, M = map(int,input().split())
light = [list(map(int,input())) for _ in range(N)]
lst = [0] * N
K=int(input())


for i in range(N):
    count = 0
    for j in range(M):
        if light[i][j] == 0:
            count+=1
    lst[i] += count
mx = 0
for i in range(N):
    same_col = 0
    if lst[i] <= K and lst[i] % 2 == K % 2:

        for j in range(N):
            if light[i] == light[j]:
                same_col += 1
    mx = max(mx, same_col)
print(mx)