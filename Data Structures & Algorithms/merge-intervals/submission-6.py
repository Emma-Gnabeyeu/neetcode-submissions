class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key = lambda x: x[0])
        if n == 1:
            return intervals
        result = [intervals[0]]
        for i in range(1,n):
            if intervals[i][0] <= result[-1][1]:
                result[-1] = [result[-1][0], max(result[-1][1],intervals[i][1])]
            else:
                result.append(intervals[i])
        return result

        