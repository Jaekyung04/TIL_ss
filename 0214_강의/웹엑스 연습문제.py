#연습문제1

# answer = 0
# num_list = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# for i in range(len(num_list)):
#     for j in range(len(num_list[0])):
#         for di, dj in [(-1,0),(1,0),(0,-1),(-1,0)]: #상하좌우
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < 5 and 0 <= nj < 5:
#                 if int(num_list[ni][nj]) > int(num_list[i][j]):
#                     gap = int(num_list[ni][nj])-int(num_list[i][j])
#                 else:
#                     gap = int(num_list[i][j]) - int(num_list[ni][nj])
#                 answer += gap
#                 print(answer)
#
# #정답
#1. 5x5 matrix 초기화
from pprint import  pprint
matrix = []
for i in range(5):
    row = [j + i* 5 for j in range(1, 6)]
    matrix.append(row)
pprint(matrix)
rlt =0
#2. 각각의 요소의 차 구하기
#2.1 각 요소에 접근하기
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        di = [-1,1,0,0]
        dj = [0,0,-1,1]
        for d in range(4):
            each_row = i + di[d]
            each_column = j + dj[d]
        #범위체크
            if each_row < 0 or each_row > 4 or each_column < 0 or each_column > 4:
               continue
            else:
            #2.2 각 요소 차 구하기
                sub = matrix[i][j] - matrix[each_row][each_column]
            #3. 절대값 처리하기
                sub = sub if sub >= 0 else - sub
            #4. 합누적하기answer +=
                rlt += sub

print(rlt)