class Solution(object):
    def convertToTitle(self, c):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = ""

        while c>0:
            c =c-1
            rem =c % 26
            res = chr(rem + ord('A'))+res
            c=c//26
        return res        
