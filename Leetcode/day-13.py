
# Longest Common Prefix
def longest_common_prefix(strs):
    if not strs:
        return ""

    strs.sort()
    first = strs[0]
    last = strs[-1]

    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]

arr = ["flower","flow","flight"]
s = longest_common_prefix(arr)
print(s)
