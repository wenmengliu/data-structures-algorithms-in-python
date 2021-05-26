class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        X = 0
        count = {0: [1, 0]}
        
        for i in range(n):
            X ^= arr[i]
            freq, ssum = count.get(X, [0, 0])
            ans += i * freq - ssum
            count[X] =  [freq + 1, ssum + i + 1]
        return ans