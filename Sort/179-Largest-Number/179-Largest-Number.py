class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """merge Sort 
        TC: O(nlogn)
        SC: O(n)
        Arguments:
            nums {List[int]} 
        
        Returns:
            str -- the largest number
        """
        sortNums = self.mergeSort(nums)
        return str(int("".join(map(str,sortNums))))
    
    def mergeSort(self, arr):
        if len(arr) <= 1: return arr
        length = len(arr) // 2
        left = self.mergeSort(arr[:length])
        right = self.mergeSort(arr[length:])
        return self.merge(left,right)
    
    def merge(self, l, r):
        i, j = 0, 0 
        res = []
        while i < len(l) and j < len(r):
            if self.compare(l[i], r[j]):
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        while i < len(l):
            res.append(l[i])
            i += 1
        while j < len(r):
            res.append(r[j])
            j += 1
        return res
            
    
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)