class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialise
        index = -1
        n = len(nums)

        # initialise start and end of search
        start = 0
        end = n-1

        while end >= start:
            mid = math.floor(end-start)

            if target == nums[mid]: 
                index = mid
                break

            elif target < nums[mid]:
                start = start
                end = mid - 1

            elif target > nums[mid]:
                start = mid + 1
                end = end

            else: 
                break
        
        return index

