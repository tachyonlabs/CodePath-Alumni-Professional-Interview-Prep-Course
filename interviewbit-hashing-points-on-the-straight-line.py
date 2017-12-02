from fractions import gcd

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        from fractions import gcd

        class Solution:
            # @param A : list of integers
            # @param B : list of integers
            # @return an integer
            def maxPoints(self, A, B):
                if len(A) <= 2:
                    return len(A)

                points = (zip(A, B))
                lines = {}
                maximum = 2

                for i in range(len(points) - 1):
                    for j in range(i + 1, len(points)):
                        num = points[j][1] - points[i][1]
                        denom = points[j][0] - points[i][0]
                        if denom == 0 and num == 0:
                            # points that have identical coordinates form their own "line"
                            # in addition to any other lines they may be in
                            intercept = points[i]
                        elif denom == 0:
                            # vertical lines
                            num = 0
                            intercept = points[j][0]
                        elif num == 0:
                            # horizontal lines
                            num = denom = None
                            intercept = points[j][1]
                        else:
                            # simplify the slope -- I thought it was easier to debug this way than just dividing it
                            the_gcd = gcd(num, denom)
                            num /= the_gcd
                            denom /= the_gcd
                            # and find the b of the y = mx + b
                            intercept = points[i][1] - ((num * 1.0) / denom) * points[i][0]
                        if (num, denom, intercept) in lines:
                            for point in [(points[i][0], points[i][1], i), (points[j][0], points[j][1], j)]:
                                if point not in lines[(num, denom, intercept)]:
                                    lines[(num, denom, intercept)].append(point)
                        else:
                            lines[(num, denom, intercept)] = [(points[i][0], points[i][1], i),
                                                              (points[j][0], points[j][1], j)]

                        maximum = max(maximum, len(lines[(num, denom, intercept)]))

                return maximum
