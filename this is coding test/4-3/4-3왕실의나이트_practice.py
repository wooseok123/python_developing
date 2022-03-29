
#1

coordinaion = input()
x_y = []
alphabet = ["a","b","c","d","e","f","g"]
for word in coordinaion:
  x_y.append(word)

if x_y[0] in alphabet:
  x_y[0] = int(alphabet.index(x_y[0]))+1

x_y[1] = int(x_y[1])

case = [[2,1],[2,-1],[-2,1],[-2,-1],[1,-2],[1,2],[-1,-2],[-1,2]]

count = 0

for x,y in case:
    
  if x_y[0] + x < 1 or x_y[0] + x > 8:
    continue
  if x_y[1] + y < 1 or x_y[1] + y > 8:
    continue

  count += 1


print(count)

#2

cordinate = input("cordinate : ")

col, line = cordinate[0], int(cordinate[1])

alphabet = {
  "a" : 1,
  "b" : 2,
  "c" : 3,
  "d" : 4,
  "e" : 5,
  "f" : 6,
  "g" : 7,
  "h" : 8
}

for key in alphabet.keys():
  if col == key :
    col = alphabet[key]

x2, x1 = [-2, 2], [-1, 1]
y2, y1 = [-2, 2], [-1, 1]

count = 0

for i in x2:
  for j in y1:
    nx = line + i
    ny = col + j
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:

      continue
    count+=1

for i in y2:
  for j in x1:
    ny = line + i
    nx = col + j
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
      continue
    count+=1

print(count)
    
    
#경우의 수를 살펴보는 습관을 들이자


