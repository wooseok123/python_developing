change = 1260

count = 0

while change > 0:
  if change >= 500:
    change -= 500
    count += 1
  if change >= 100 and change < 500:
    change -= 100
    count += 1
  if change >= 50 and change < 100:
    change -= 50
    count += 1
  if change >= 10 and change < 50:
    change -= 10
    count += 1

print(count);
