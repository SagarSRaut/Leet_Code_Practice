class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # h=0       
        # for i in range(len(nums)):
        #     if nums[i]!=val:
        #         nums[h]=nums[i]
        #         h+=1
            
        i=0 
        while (i<len(nums)):
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)