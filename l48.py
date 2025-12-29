##ROTATE IMAGE
##STATS: BEATS 100% in speed, 94.5% in storage
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)-1
        holder = 0
        for d in range(int(len(matrix)//2)):
            for i in range(d,l-d):
                prev = matrix[d][i]
                holder = 0
                x, y = d, i
                px, py  = x, y
                for k in range(4):
                    holder = matrix[y][l-x]

                    matrix[y][l-x] = prev
                    prev = holder
                    # y = n
                    # x = 0
                    # How do you get x = n, and y = 0

                    x = py
                    y = l-px
                    px = x
                    py = y

