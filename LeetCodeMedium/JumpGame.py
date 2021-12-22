from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # return self.canJumpBackTrack(0, nums)
        memo = ["U"] * len(nums)
        memo[len(nums)-1] = "G"
        return self.canJumpMemo(0, nums, memo)

    def canJumpMemo(self, position, nums, memo):
        if memo[position] != "U":
            return True if memo[position] == "G" else False

        maxJump = min(position + nums[position], len(nums) - 1)
        for nextPos in range(maxJump, position, -1):
            if self.canJumpMemo(nextPos, nums, memo):
                memo[position] = "G"
                return True

        memo[position] = "B"
        return False

    def canJumpBackTrack(self, position, nums):
        # print(position)
        if position == len(nums) - 1:
            return True

        jump = min(position + nums[position], len(nums) - 1)
        for i in range(position + 1, jump+1):
            # for i in range(jump , position+1, -1):
            if self.canJumpBackTrack(i, nums):
                return True
        else:
            return False

    def canJumpBottomUp(self, nums):
        n = len(nums)
        memo = [False] * len(nums)
        memo[n - 1] = True
        for idx in range(n-2, -1, -1):
            maxJumpFromidx = min(idx + nums[idx], n-1)
            for step in range(idx + 1, maxJumpFromidx+1):
                if memo[step]:
                    memo[idx] = True
                    break

        return memo[0]

    def canJumpGreedy(self, nums):
        n = len(nums)
        lgidx = n - 1
        for idx in range(n - 2, -1, -1):
            # maxJumpFromidx = min(idx + nums[idx],n - 1)
            if idx + nums[idx] >= lgidx:
                lgidx = idx
        return lgidx == 0


s = Solution()
res = s.canJumpGreedy([2, 3, 1, 1, 4])
# res = s.canJumpBottomUp([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6])
# res = s.canJump([2,0])
print(res)
