

# Text Justification
class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)

        while i < n:
           
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            line = ""
            num_words = j - i
            is_last_line = j == n

            if num_words == 1 or is_last_line:
              
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                
                total_spaces = maxWidth - line_len
                space_between_words = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)

                for k in range(num_words):
                    line += words[i + k]
                    if k < num_words - 1:
                        spaces = space_between_words + (1 if k < extra_spaces else 0)
                        line += " " * spaces

            res.append(line)
            i = j

        return res


sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
result = sol.fullJustify(words, maxWidth)
for line in result:
    print(f'"{line}"')