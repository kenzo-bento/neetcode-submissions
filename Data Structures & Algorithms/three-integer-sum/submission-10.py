class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        final = []
        print(sorted_nums)
        for tp in range(len(nums) - 2):
            if tp != 0 and sorted_nums[tp] == sorted_nums[tp - 1]:
                continue
            lp = tp + 1
            rp = len(sorted_nums) - 1
            while lp < rp:
                if sorted_nums[tp] + sorted_nums[rp] + sorted_nums[lp] == 0:
                    final.append([sorted_nums[tp], sorted_nums[rp], sorted_nums[lp]])
                    lp += 1
                    rp -= 1

                    while lp < rp and sorted_nums[lp] == sorted_nums[lp - 1]:
                        lp += 1

                    while lp < rp and sorted_nums[rp] == sorted_nums[rp + 1]:
                        rp -= 1
                elif sorted_nums[tp] + sorted_nums[rp] + sorted_nums[lp] > 0:
                    rp -= 1
                else:
                    lp += 1
        
        return final
            