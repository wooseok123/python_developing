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