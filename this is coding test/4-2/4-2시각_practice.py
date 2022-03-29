n = int(input("number : "))

count = 0
second = 0
minute = 0
hour = 0


while hour <= n:

  time = f'{hour}{minute}{second}'

  if "3" in time:
    count +=1
    
  second += 1

  if second == 60:
    second = 0
    minute += 1

  if minute == 60:
    minute = 0
    hour += 1

print(count)


  