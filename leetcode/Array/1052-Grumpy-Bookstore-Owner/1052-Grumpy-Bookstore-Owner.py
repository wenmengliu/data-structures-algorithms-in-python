class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        base, window, best_window = 0, 0, 0
        for i in range(len(grumpy)):
            # not satisfied
            if grumpy[i]:
                window += customers[i]
            # already satisfied
            else:
                base += customers[i]
            # a rolling sum of the last X customers in the array,
            if i >= X and grumpy[i-X] == 1:
                window -= customers[i-X]
            
            best_window = max(best_window, window)
        
        return base + best_window
# TC: O(n)
# SC: O(1)