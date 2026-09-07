class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        li=[]
        for i in range(0,len(nums)):
            re=target-nums[i]
            if re in dic:
                li.extend([nums.index(re),i])
            dic[nums[i]]=i
        return li
    
        
            
        