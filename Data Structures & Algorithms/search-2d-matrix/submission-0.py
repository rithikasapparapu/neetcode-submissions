class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) #3
        m = len(matrix[0]) #4
        l, r = 0, n*m - 1
        while l <= r:
            mid = (l+r)//2
            q = mid // m
            rem = mid % m
            if matrix[q][rem] == target:
                return True
            elif matrix[q][rem] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False



        