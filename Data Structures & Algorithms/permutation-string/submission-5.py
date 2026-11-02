class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        if not s1:
            return True

        if not s2:
            return False

        lookup = defaultdict(int)

        for char in s1:
            lookup[char] += 1


        lp = 0
        rp = len(s1) - 1

        placeholder = defaultdict(int)

        for char in s2[lp:rp+1]:
            placeholder[char] += 1

        while rp < len(s2) - 1:
            if lookup == placeholder:
                return True
            
            placeholder[s2[lp]] -= 1
            if placeholder[s2[lp]] == 0:
                del placeholder[s2[lp]]
            lp += 1
            rp += 1
            placeholder[s2[rp]] += 1

        if lookup == placeholder:
                return True
        return False
