class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        data=set()
        for i in range(len(nums)):
            if nums[i] in data:
                return True
            else:
                data.add(nums[i])
        return False