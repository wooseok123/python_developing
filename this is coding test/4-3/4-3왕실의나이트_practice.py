
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



