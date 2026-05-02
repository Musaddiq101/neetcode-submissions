class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        ans = [1]*len(nums)
        for i in range(len(nums)):
            print(prev)
            ans[i] = prev * ans[i]
            prev *= nums[i]
        
        print(ans)
        
        prev = 1
        for i in range(len(nums)-1, -1,-1):
            ans[i] = prev * ans[i]
            prev *= nums[i]

        return ans
        