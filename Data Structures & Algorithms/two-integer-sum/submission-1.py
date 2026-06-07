class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []
        solution = []

        for index, number in enumerate(nums):
            difference = target - number
            if difference in seen:
                idx1 = seen.index(difference)
                idx2 = index
                solution = [idx1, idx2]
                return solution
            else: 
                seen.append(number)
        return solution