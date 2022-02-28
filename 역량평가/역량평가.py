import sys

sys.stdin = open('sample_input (2).txt')

di = [-1,0,0,1]
dj = [0,1,-1,0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(tc,N, arr)
    answer = 0
    gi, gj = 0, 0
    wall = 0
    secure = 0
    p = 1
    d = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                wall += 1

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                gi, gj = i, j
                while d < 4:
                    ni, nj = gi+di[d]*p, gj+dj[d]*p
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 0:
                            secure += 1
                            p += 1
                        else:
                            d += 1
                            p = 1
                    else:
                        d += 1
                        p = 1
    answer = N**2 - wall - secure - 1
    print(f'#{tc} {answer} {wall} {secure}')