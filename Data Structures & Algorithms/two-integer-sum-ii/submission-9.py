class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = lp + 1
        next_lp = 0
        while lp < len(numbers) - 1:
            if rp == len(numbers):
                    lp += 1
                    rp = lp + 1
            if numbers[lp] + numbers[rp] == target:
                return [lp + 1, rp + 1]
            if numbers[lp] == numbers[rp]:
                lp = rp
            rp += 1
        