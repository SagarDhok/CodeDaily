
# Number of Lines To Write String
def numberOfLines(widths, s):
    lines = 1  
    current_width = 0  

    for char in s:  
        w = widths[ord(char) - ord('a')] 
        if current_width + w > 100:
            lines += 1  
            current_width = w  
        else:
            current_width += w 

    return [lines, current_width]  

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
print(numberOfLines(widths,s))

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"
print(numberOfLines(widths,s))