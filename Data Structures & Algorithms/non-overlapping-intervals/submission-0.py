class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda item: item[0])
        i = 1
        count = 0
        while i < len(intervals):
            if intervals[i-1][1] <= intervals[i][0]:
                i += 1
            else:
                if intervals[i-1][1] > intervals[i][1]:
                    intervals.pop(i-1)
                else:
                    intervals.pop(i)
                count += 1
        return count

        