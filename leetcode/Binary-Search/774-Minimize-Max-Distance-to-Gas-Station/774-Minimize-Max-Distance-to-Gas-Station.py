class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        l, r = 0, stations[-1]-stations[0]
        while r - l > 1e-6:
            m = (r+l)/2.0
            cuts = 0
            for s1, s2 in zip(stations, stations[1:]):
                cuts += int((s2-s1)/m)
            if cuts <= k:
                r = m
            else:
                l = m 
        return l