class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l=min(nums)
        m=max(nums)
        a=[]
        for i in range(l,m):
            if i not in nums:
              a.append(i)
        return sorted(a)
