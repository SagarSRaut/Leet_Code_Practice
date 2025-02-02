class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=nums[0]
        count=1
        for i in nums[1:]:
            if i==candidate:
                count+=1
            else:
                if count==0:
                    candidate=i
                    count=1
                else:
                    count-=1
        return candidate
        