class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        i,j=0,1
        ans = [0] * len(nums)
        for num in nums:
            if num>0:
                ans[i] = num
                i+=2
            else:
                ans[j]=num
                j+=2
        return ans 