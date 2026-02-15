class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in range(len(nums)):
            if nums[i]==1:
                a+=1 
            else:
                a=0
            b=max(a,b)
        
        return b
                          
        