class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = []
        for row in board:
            lis = []
            for s in row:
                if s == ".":
                    lis.append(0)
                else:
                    lis.append(int(s))
            nums.append(lis)
        for i in range(9):
            s = set()
            for j in range(9):
                if nums[i][j] != 0:
                    if nums[i][j] in s:
                        return False
                    s.add(nums[i][j])
        for j in range(9):
            s = set()
            for i in range(9):
                if nums[i][j] != 0:
                    if nums[i][j] in s:
                        return False
                    s.add(nums[i][j])
        for i in range(0,9,3):
            for j in range(0,9,3):
                s = set()
                for _ in range(3):
                    for _ in range(3):
                        if nums[i][j] != 0:
                            if nums[i][j] in s:
                                return False
                            s.add(nums[i][j])
                        j += 1
                    j -= 3
                    i += 1
                i -= 3
        return True

            


        