class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        countb=0
        deletions=0

        for ch in s:
            if ch=='b':
                countb += 1

            else:
                deletions=min(deletions+1,countb)
        
        return deletions


############################# Logic #########################################
# so in thie question my logic is to count number of b if the input string starts with b and then followed by a's so in this in the else statement we are finding the minimum munber of deletions 
