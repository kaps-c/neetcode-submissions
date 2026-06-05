class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[j] == nums[i]: # therefore they're the same
                    return True

                else:
                    j+= 1 

            i += 1 # increase i by 1 to check next iter

        return False # default return if no duplicates

