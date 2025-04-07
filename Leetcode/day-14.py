
#Merge string array alternatively
word1 = "abcd"
word2 = "pq"
s = ""
i = 0
while i<len(word1) or i<len(word2):
   if i<len(word1):
      s += word1[i]
   if i <len(word2):
      s +=word2[i]
   i = i+1
print(s)