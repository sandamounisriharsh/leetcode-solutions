class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in range(len(nums)):
            if nums[i]==1:
                a+=1 
                b=max(a,b)
            else:
                a=0
        return b
                          
        