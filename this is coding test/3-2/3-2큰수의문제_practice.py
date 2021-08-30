n_number,m,k = "5 8 3".split()
n_list = "2 4 5 4 6".split()
new_nlist = []
for number in n_list:
  number = int(number)
  new_nlist.append(number)

count = 0
total = 0

m = int(m)
k = int(k)

max1_number = max(new_nlist)
new_nlist.remove(max1_number)
max2_number = max(new_nlist)

while count < m :
  if max1_number > max2_number :
    i= 0
    while i < k :
      total += max1_number
      i+=1
      count += 1
    total += max2_number
    count+=1

  if max1_number == max2_number:
    total = max1_number * m

print(total)
    

# 성능 측정 :  0.007951021194458008


  

