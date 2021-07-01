from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast


s = Solution()
print(s.findDuplicate([2,5,4,6,9,3,8,9,7,1]))
# print(s.findDuplicate([1,3,4,2,2]))
