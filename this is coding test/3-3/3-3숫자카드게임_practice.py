

n, m = map(int,input("첫번째 줄 :").split())

min_list = []

for i in range(n):
  row = list(map(int,input("두번째 줄 :").split()))
  min_list.append(min(row))

max_num = max(min_list)

print(max_num)

