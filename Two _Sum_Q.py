class Two_sum:
    def element(self,nums,target):
        """
        num: list 
        target: int
        returnType: list
        """
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]+nums[j]==target):
                    return [i,j]
        return[]      

t=Two_sum()
result=t.element([4,3,2],6 )
print(result)

    


