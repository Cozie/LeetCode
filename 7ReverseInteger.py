class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        s=1
        
        if x<0:
            x=-x
            s=-1

        ans=int(str(x)[::-1])

        if ans< pow(2,31):
            return ans*s
        else:
            return 0
