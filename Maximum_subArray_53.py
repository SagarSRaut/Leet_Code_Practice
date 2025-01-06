class Solution:
    def maxSubArray(self, nums):
        sum1=0
        maxi=nums[0]
        for i in range(len(nums)):
            sum1+=nums[i]
            maxi=max(maxi,sum1)

            if sum1<0:
                sum1=0
        return maxi  

d=Solution()
res=d.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)