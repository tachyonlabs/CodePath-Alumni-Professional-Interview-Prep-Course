# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#     def __repr__(self):
#         return "[{}, {}]".format(self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda x: (x.start, x.end))
        not_processed = {intv: 1 for intv in intervals}
        merged = []
        for i in range(len(intervals)):
            if intervals[i] in not_processed:
                for j in range(i + 1, len(intervals)):
                    if intervals[j].start >= intervals[i].start and intervals[j].start <= intervals[i].end:
                        intervals[i].end = max(intervals[i].end, intervals[j].end)
                        del not_processed[intervals[j]]
                    else:
                        break

                merged.append(intervals[i])

        return merged
