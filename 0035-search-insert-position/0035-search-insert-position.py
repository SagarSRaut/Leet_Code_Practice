class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):

            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
        return l
        # left = 0
        # right = len(nums) - 1

        # while left <= right:
        #     mid = (left + right) // 2

        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        
        # return left
         