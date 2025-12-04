class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows > len(s):
            return s
        cur = 0
        ff = [""]*numRows
        dir = -1
        for i in s:
            ff[cur]+=i
            if cur == 0 or cur == numRows - 1:
                dir *= -1
            cur+=dir

        return "".join(ff)
