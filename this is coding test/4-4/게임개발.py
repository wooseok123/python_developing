n, m = map(int, input("n, m : ").split(" "))
x, y, d = map(int, input("x, y, dir : ").split(" "))

corList = []

dirX = [-1, 0, 1, 0]
dirY = [0, 1, 0, -1]

visitedCor = []

for i in range(n):
  corList.append(list(map(int, input().split(" "))))

print(corList)
realD = d

breakCount = 0
result = 0

while True:

  if breakCount == 4:
    if realD == 0:
      realD == 2
    elif realD == 1:
      realD == 3
    else :
      realD -= 2

    nx = x + dirX[realD]
    ny = y + dirY[realD]
    x, y = nx, ny
    result +=1
    
    nx = x + dirX[realD]
    ny = y + dirY[realD]
    
    if corList[nx][ny] == 1:
      break
    
  
  if realD == 3:
    realD = 0      
  else:
    realD += 1
      
  nx = x + dirX[realD]
  ny = y + dirY[realD]

  if corList[nx][ny] == 1:
    breakCount += 1
    continue
  elif (nx, ny) in visitedCor:
    breakCount += 1
    continue
  else:
    breakCount = 0
    result += 1
    x = nx
    y = ny
    visitedCor.append((x,y))
    print(x,y)

print(result)
      
        