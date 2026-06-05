from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
            
        cnt = Counter(nums)
        mode = cnt.most_common(1)[0][1]
        if mode > 1:
            return True
        return False
        