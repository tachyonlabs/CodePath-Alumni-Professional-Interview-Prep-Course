class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        # I made departure greater than arrival so that with same-day arrivals and departures, the
        # departures will be sorted ahead of the arrivals,
        arrival, departure = 1, 0
        dates = sorted([(arr, arrival) for arr in arrive] + [(dep, departure) for dep in depart])
        guests = 0
        for date, which in dates:
            if which == arrival:
                guests += 1
                if guests > K:
                    return 0
            else:
                guests -= 1

        return 1
