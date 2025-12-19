class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        valid = [-1, -1]
        if len(nums) == 1 and nums[0]==target:
            return [0, 0]
        while r>=l:
            mid = int(l + (r-l)/2)
            print("My middle" + str(mid))
            if nums[mid]>target:
                r = mid-1
                mid = int(l + (r-l)/2)
            elif nums[mid]<target:
                l = mid+1
                mid = int(l + (r - l)/2)
            else:
                print("Foound the number at INDEX " + str(mid))
                valid = [mid, mid]
                p = mid-1
                while 0<=p and nums[p]==target:
                    valid[0] = p
                    p-=1
                d = mid+1
                while d<len(nums) and nums[d]==target:
                    valid[1] = d
                    d+=1
                break
        return valid       

