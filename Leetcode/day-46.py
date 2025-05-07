


# Reverse Vowels of a String
s = input("Enter A String: ")
vowels = "aeiouAEIOU"  
vowel_list = [i for i in s if i in vowels]  
vowel_list.reverse()  

res = [] 

vowel_index = 0

for i in s:
    if i in vowels: 
        res.append(vowel_list[vowel_index])  
        vowel_index += 1
    else:
        res.append(i)  

print("".join(res))
