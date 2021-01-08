class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in reversed(nums):
            if i == val:
                nums.remove(i)
        return len(nums)