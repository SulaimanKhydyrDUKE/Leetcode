class Solution(object):
    def maximumTripletValue(self, nums):
        leftMax = [nums[0]]*len(nums)
        rightMax = [nums[len(nums)-1]]*len(nums)
        l, r, = 0, len(nums)-1
        rmax = 0
        lmax = 0
        for i in nums:
            rightMax[r] = rmax
            leftMax[l] = lmax
            lmax = max(lmax, nums[l])
            
            
            rmax = max(rmax, nums[r])
            
            r-=1
            l+=1
        maks = 0
        print("LeftMax" + str(leftMax))
        for b in range(len(nums)):
            maks = max(maks, (leftMax[b]-nums[b])*rightMax[b])
        return maks



        
