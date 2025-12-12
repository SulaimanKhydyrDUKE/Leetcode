
## This solution might be wrong, I need to reimplement it
class Solution(object):
    def threeSumClosest(self, nums, target):
        # 1) Sort it
        nums.sort()
        print("SORTED ARRAY: " + str(nums))
        # 2) Two pointers 
        ret = nums[0] + nums[1] + nums[2]
        close = abs( target - ret)
        l,m, r = 0, 1, 2
        while r<len(nums)-1 and l!=r and m!=l and r!=m:
            temp = abs(target - (nums[r+1] + nums[l] + nums[m]))
            if temp < abs(target - close):
                close = temp
                r+=1
            else:
                return close
            temp = abs(abs(target) - abs((nums[r] + nums[l] + nums[m+1])))
            if temp < abs(target - close):
                close = temp
                m+=1
            else:
                return close
            temp = abs(target - (nums[r] + nums[l+1] + nums[m]))
            if temp < abs(target - close):
                close = temp
                l+=1
            else:
                return close
        return close
            

