def solution(s):
    answer = ""
    letter = ""
    numbers = {"zero" : 0,
               "one" : 1,
               "two" : 2,
               "three" : 3,
               "four" : 4,
               "five" : 5,
               "six" : 6,
               "seven" : 7,
               "eight" : 8,
               "nine" : 9}

    for i in range(len(s)):
      if s[i].isdigit():
          answer += s[i]
      else:
          letter += s[i]

      if letter in numbers.keys():

          answer += str(numbers[letter])
          letter = ""
    return answer

