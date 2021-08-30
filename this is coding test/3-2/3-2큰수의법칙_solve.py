n, m , k = map(int, "5 8 3".split())

data = list(map(int, "2 4 5 4 6".split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True :
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)

# 성능 측정 :  0.009973287582397461