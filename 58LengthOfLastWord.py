class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):

        while (len(s)>0 and s[-1]==' '):
            s = s[:-1]

        a=0
        if len(s) != 0:
            i=len(s)-1
#            a=0
            while (s[i] != ' ' and i > -1):
                a=a+1
                i=i-1
#        else:
#            return 0
            
        return a
