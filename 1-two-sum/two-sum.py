class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        right = len(nums)-1
        arr = [(nums[i],i) for i in range(len(nums))]
        left=0
        arr.sort()

        while(left<right):
            sum = arr[left][0]+arr[right][0]
            if(sum==target):
                return [arr[left][1],arr[right][1]]

            if(sum>target):
                right-=1

            else:
                left+=1
        
        