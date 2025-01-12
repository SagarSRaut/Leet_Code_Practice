class Bubble:
    
    def bubble_sort(self,num):
        n=len(num)
        for i in range(n):
            for j in range(n-1):
                if num[j]>num[j+1]:
                    temp=num[j]
                    num[j]=num[j+1]
                    num[j+1]=temp
        return num


b=Bubble()
v=[40,70,30,80,100]
print(b.bubble_sort(v))