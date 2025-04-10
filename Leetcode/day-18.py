#  "Plus One to an Integer Represented as Array"
def plusone(digits):
  for i in range(len(digits)-1,-1,-1):
    if digits[i]<9:
       digits[i]+=1
       return digits
    digits[i] = 0

  return [1]+digits

digits = [9,9]
print(plusone(digits))