class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        a = []
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            if(i>0 and nums[i-1]==nums[i]):
                continue
            while(j<k):
                sum = nums[i]+nums[j]+nums[k]
                if(sum==0):
                    a.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and nums[k]==nums[k+1]):
                        k-=1

                elif(sum<0):
                    j+=1
                else:
                    k-=1


        
        return a
