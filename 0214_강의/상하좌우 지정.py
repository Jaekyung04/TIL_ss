#NxM 배열
# di = [0, 1, 0, -1] #오른쪽부터 시계방향으로 0, 1, 2, 3 일때
# dj = [1, 0, -1, 0]
# for k in range(4):
#     ni = i + di[k]
#     nj = j + dj[k]  #현재위치가 ij일 때, 행과열의 값이 (ni, nj)
#     if 0<=ni<N and 0<=nj<M
#         arr[ni][nj]
#
# #2번째 방법
# for di, dj in[(0,1), (1,0),(0,-1),(-1,0)]:
#     ni = i + di
#     nj = j + dj
#     if 0<=ni<N and 0<=nj<M: #유효 인덱스
#         arr[ni][nj]

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = 3
for i in range(N):
    for j in range(N):
        for di, dj in [(-1,0),(1,0),(0,-1),(-1,0)]: #상하좌우
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<= nj<N:  # 유효 인덱스
                print(i, j, arr[ni][nj])
        print()