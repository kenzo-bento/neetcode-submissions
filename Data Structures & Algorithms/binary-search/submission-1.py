class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        print(target)
        while lp <= rp:
            middle = (lp + rp) // 2
            print(nums[middle])
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                lp = middle + 1
            else:
                rp = middle - 1
        
        return -1