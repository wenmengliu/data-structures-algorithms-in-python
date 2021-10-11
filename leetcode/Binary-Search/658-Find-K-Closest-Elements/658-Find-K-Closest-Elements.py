class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        # use binary search to search for the starting point of result subarry
        # O(log(n - k))
        while left < right:
            mid = left + (right - left)//2
            
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid 
            else:
                left = mid + 1
        return arr[left: left + k]