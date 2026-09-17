class Solution:
    def sortColors(self, nums):
        count0=0
        count1=0
        count2=0
        for i in nums:
            if i==0:
                count0+=1
            elif i==1:
                count1+=1
            else:
                count2+=1
        nums[0:count0]=[0] * count0
        nums[count0:count1+count2] =[1]*count1
        nums[count0+count1:] = [2] * count2
        