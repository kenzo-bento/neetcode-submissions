class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for matrices in matrix:
            if target in matrices:
                return True
        return False