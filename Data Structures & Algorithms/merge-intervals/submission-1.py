class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda item: item[0])
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] >= intervals[i][0]:
                interval = [intervals[i-1][0], max(intervals[i-1][1], intervals[i][1])]
                intervals.pop(i)
                intervals.pop(i-1)
                intervals.insert(i-1, interval)
            else:
                i += 1
        return intervals

        