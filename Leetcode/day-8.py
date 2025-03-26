
# Check if a String is a Valid Palindrome
s = input("Enter Your Sentence : ")
s1 = ""
for i in s:
     if i.isalnum(): 
          s1 = s1+i.lower()
if s1 == s1[::-1]:
     print(True)
else:
     print(False)


#or

s = input("Enter Your Sentence : ")
s1 = "".join(i.lower() for i in s if i.isalpha()) 
print(s1 == s1[::-1])  
