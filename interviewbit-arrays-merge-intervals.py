# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#     def __repr__(self):
#         #return "({}, {})".format(self.start, self.end)
#         return "(%d, %d) " %(self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        if new_interval.start > new_interval.end:
            new_interval.start, new_interval.end = new_interval.end, new_interval.start
        interval_inserted = False
        merged = []
        for interval in intervals:
            if not interval_inserted:
                for i1, i2 in [[interval, new_interval], [new_interval, interval]]:
                    if (i1.start >= i2.start and i1.start <= i2.end) or (i1.end >= i2.start and i1.end <= i2.end):
                        interval.start, interval.end = min(interval.start, new_interval.start), max(interval.end, new_interval.end)
                        interval_inserted = True
                        break
                merged.append(interval)
            else:
                if merged and (interval.start >= merged[-1].start and interval.start <= merged[-1].end) or (merged[-1].end >= interval.start and merged[-1].end <= interval.end):
                    merged[-1].start, merged[-1].end = min(interval.start, merged[-1].start), max(interval.end, merged[-1].end)
                else:
                    merged.append(interval)


        if not interval_inserted:
            merged.append(new_interval)

        return sorted(merged, key=lambda x: x.start)
