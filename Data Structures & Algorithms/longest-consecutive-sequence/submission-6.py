class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        maxLen = 0
        length = 1;
        for num in nums:
            if num-1 not in seen:
                length = 1
                while num+1 in seen:
                    length += 1
                    num += 1
                
                maxLen = int(max(maxLen, length))

        return maxLen
            


