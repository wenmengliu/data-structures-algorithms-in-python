class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(l,h,-1,i) for i, (l,r,h) in enumerate(buildings)] + \
        [(r,h,1,i) for i, (l,r,h) in enumerate(buildings)]
        # sort the events
        events.sort(key=lambda x: (x[0], x[1]*x[2]))
        # in python heaps are minimum heaps so we need to keep negative height
        hp, cur, ans = [(0,-1)], set([-1]), []
        
        for x, h, tp, ind in events:
            if tp == -1:
                cur.add(ind)
                if h > -hp[0][0]:
                    ans.append([x,h])
                heappush(hp,(-h, ind))
            else:
                cur.remove(ind)
                # remove all inactive elements from heap
                if h == -hp[0][0]:
                    while hp and hp[0][1] not in cur: heappop(hp)
                if -hp[0][0] != ans[-1][1]:
                    ans.append([x, -hp[0][0]])
        
        return ans