
# Count Vowel Substrings of a String
def countVowelSubstrings(word: str) -> int:
    vowels = "aeiou"
    count = 0
    
    for i in range(len(word)):
        for j in range(i, len(word)):
            substring = word[i:j+1]
            if all(v in substring for v in vowels) and all(c in vowels for c in substring):
                count += 1
                
    return count
print(countVowelSubstrings("aeiouu"))       
print(countVowelSubstrings("unicornarihan")) 
print(countVowelSubstrings("cuaieuouac"))   
