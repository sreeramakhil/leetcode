class Solution(object):
    def titleToNumber(self, c):
        """
        :type columnTitle: str
        :rtype: int
        """
        res=0

        for ch in c:
            value = ord(ch)-ord("A")+1
            res=res*26+value

        return res

        
