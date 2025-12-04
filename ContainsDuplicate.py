class Solution(object):
    def containsDuplicate(self, nums):
        map = {} 
        for i in nums:
            if i in map:
                return True 
            map[i] = 1
        return False
        
