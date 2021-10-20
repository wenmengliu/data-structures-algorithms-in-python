class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area, corners = 0, set()
        for x1,y1,x2,y2 in rectangles:
            area += (x2-x1) * (y2-y1)
            # the external corners must appear only once, and the ones inside have to be an even number (we filter them with xor)
            corners ^= {(x1,y1), (x1,y2), (x2,y1), (x2,y2)}
        if len(corners) != 4: return False
        X1, Y1 = min(corners, key = lambda x: x[0] + x[1])
        X2, Y2 = max(corners, key = lambda x: x[0] + x[1])
        
        return area == (X2-X1)*(Y2-Y1)