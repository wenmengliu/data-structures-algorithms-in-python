class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = { '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y
            }
        
        def ways(s):
            ans = []
            for i in range(len(s)):
                if s[i] in '-+*':
                    ans += [ops[s[i]](l,r) for l, r in itertools.product(ways(s[:i]), ways(s[i+1:]))]
            if not ans: ans.append(int(s))
            return ans  
        return ways(expression)

# TC: O(N*2^N)
# SC: O(N)