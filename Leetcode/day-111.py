

#! 832. Flipping an Image
class Solution:
    def flipAndInvertImage(self, image):
        for row in image:
            for i in range((len(row) + 1) // 2):
                row[i], row[-1 - i] = 1 - row[-1 - i], 1 - row[i]
        return image

s= Solution()


image = [[1,1,0],[1,0,1],[0,0,0]]
print(s.flipAndInvertImage(image))

image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(s.flipAndInvertImage(image))