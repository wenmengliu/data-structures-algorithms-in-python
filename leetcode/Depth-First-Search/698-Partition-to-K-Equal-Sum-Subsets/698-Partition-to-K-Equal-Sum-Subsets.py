class Solution:    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if(total%k):
            return False
        target = total // k
        n = len(nums)
        # sort the array in case of repetitively comparison on the same number
        nums.sort(reverse=True)
        visited = [0 for _ in range(n)]
        
        def dfs(cur, group, ssum):
            if group == k:
                return True
            if ssum > target: 
                return False
            if ssum == target:
                return dfs(0, group + 1, 0)
            last = -1
            for i in range(cur, n):
                if nums[i] == last or visited[i] == 1:
                    continue
                visited[i] = 1
                last = nums[i]
                if dfs(i, group, ssum + nums[i]):
                    return True
                # backtracking
                visited[i] = 0
            return False
        return dfs(0,0,0)