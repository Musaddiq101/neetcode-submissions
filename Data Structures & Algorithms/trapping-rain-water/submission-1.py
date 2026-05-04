class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        maxLs = [0] * n
        maxRs = [0] * n


        lMax = 0
        for i in range(n):
            if i > 0:
                lMax = max(lMax, height[i-1])
                maxLs[i] = lMax

        rMax = 0
        for i in range(n-1,-1,-1):
            if i < n-1:
                rMax = max(rMax, height[i+1])
                maxRs[i] = rMax


        for i in range(n):
            res = min(maxLs[i], maxRs[i]) - height[i]
            if res > 0:
                water += res


        return water 
        