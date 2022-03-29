#1

N = map(int,input())
directions = list(map(str,input().split()))

first = [1,1]

for direction in directions:
     if direction == "L":
       if first[1] == 1:
        continue
       else :
        first[1] -= 1
      
     if direction == "R":
        if first[1] == N:
          continue
        else :
          first[1] += 1
      
     if direction == "U":
        if first[0] == 1:
          continue
        else :
          first[0] -= 1

     if direction == "D":
        if first[0] == N:
          continue
        else :
          first[0] += 1
        
print(first[0],first[1])

#2

n = int(input("number :"))

dirList = list(map(str, input("directions :").split(" ")))

x = 1
y = 1

for dir in dirList:
  if x < 1:
    x +=1
  if y < 1:
    y +=1
  if x > n:
    x -=1
  if y > n:
    y -=1

  if dir == "L":
    y -= 1
  elif dir == "R":
    y += 1
  elif dir == "U":
    x -= 1
  else:
    x += 1 

print(x,y)

#모범답안

n = int(input("number :"))

dirList = list(map(str, input("directions :").split(" ")))

x, y = 1, 1

dx = [0,0,-1,1]
dy = [1,-1,0,0]

directions = ["R","L","U","D"]

for dir in dirList:
  for i in range(len(directions)):
    if dir == directions[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue

  x, y = nx, ny

print(x,y)