class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        
        for i in range(n):
            ans = round(target/n)
            if ans < arr[i]: return ans 
            target -= arr[i]
            n -= 1
            
        return arr[-1]