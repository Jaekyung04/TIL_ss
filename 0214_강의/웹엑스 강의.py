#행 우선순회
num_list = [[1, 2, 3,],[4,5,6],[7,8,9]]

for i in range(len(num_list)):  #row의 수
    for j in range(len(num_list[0])): #column의 수
        print(num_list[i][j], end=" ")

#delta를 이용한 순회

from pprint import pprint

num_list = [[1,2,3],[4,5,6],[7,8,9]]
print(num_list)
pprint(num_list, indent=4, width=15)

#상하좌우 출력 코드 (5일 때, 상하좌우)

# from pprint import pprint
#
num_list = [[1,2,3],[4,5,6],[7,8,9]]
print(num_list)
pprint(num_list, indent=4, width=15)
#
  for i in range(len(num_list)):  #row의 수
    for j in range(len(num_list[0])): #column의 수
         if num_list[i][j] == 5:
            print(num_list[i-1][j]) #상
            print(num_list[i+1][j]) #하
            print(num_list[i][j-1]) #좌
            print(num_list[i][j+1]) #우
        print(num_list[i][j], end=" ")

            di = [-1, 1, 0, 0]
            dj = [0, 0, -1, 1]
            for d in range(4):
                each_row = i + di[d]
                each_column = j + dj[d]
                print(num_list[each_row][each_column])