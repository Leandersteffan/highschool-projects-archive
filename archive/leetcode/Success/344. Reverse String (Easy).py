class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            l_to_r = s.pop(l)
            r_to_l = s.pop(r - 1)
            s.insert(l, r_to_l)
            s.insert(r, l_to_r)
            l, r = l + 1, r - 1
            
        '''s.reverse()'''
