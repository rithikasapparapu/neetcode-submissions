class Solution:
    def isPalindrome(self, s: str) -> bool:
        lis = [ch for ch in s.lower() if ch.isalnum()]
        if len(lis)==0: return True
        i = 0
        j = len(lis) - 1
        while i < j:
            if lis[i] != lis[j]:
                return False
            i += 1
            j -= 1
        return True

        