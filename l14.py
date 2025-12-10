class Solution(object):
    def longestCommonPrefix(self, strs):
        s_strs = sorted(strs, key = len)
        ret = s_strs[0]
        for i in range(len(s_strs)):
            if i+1<len(s_strs):
                temp = ""
                for k in range(len(s_strs[i])):
                    if s_strs[i][k] == s_strs[i+1][k]:
                        temp+=s_strs[i][k]
                    else: 
                        break 
                if len(temp)<len(ret):
                    ret = temp
        return ret
                    
#This is a very slow implementation due to sorting done for each item, but I will put a code without sorting in the bottom -->
