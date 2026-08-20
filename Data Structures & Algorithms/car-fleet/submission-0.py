class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p, s in sorted(list(zip(position, speed)))[::-1]:
            time = (target - p)/s
            while not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
                






        