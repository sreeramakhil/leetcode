class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone={
            "2" :"abc",
            "3" :"def",
            "4" :"ghi",
            "5" :"jkl",
            "6" :"mno",
            "7" :"pqrs",
            "8" :"tuv",
            "9" :"wxyz"
        }
        res= [""]
        for digit in digits :
            t= []
            for combination in res:
                for letter in phone[digit]:
                    t.append(combination+letter)
            res =t
        return res

## by using the hashing function 
