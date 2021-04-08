class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        :type preorder: str
        :rtype: bool
        """
        p = preorder.split(',')
        # At the start there is one available slot
        slot = 1
        for node in p:
            # No slot left to consume current node
            if slot == 0:
                return False
            if node == '#':
                # null node consumes one slot
                slot -= 1
            else:
                # non-null node consumes one slot and adds two more slots
                slot += 1
        # At the last, we should keep empty slot if it is valid
        return slot==0

# TC: O(N)
# SC: O(1)