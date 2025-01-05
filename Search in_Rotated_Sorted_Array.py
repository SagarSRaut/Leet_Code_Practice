class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
    
s=Solution()
res=s.search([2,3,5,6,8,9,4],8)
print(res)