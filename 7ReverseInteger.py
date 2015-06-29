class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        s=1
        
        if x<0:
            x=-x     # convert negative into positive integer
            s=-1     # mark as negative

        ans=int(str(x)[::-1])

        if ans< pow(2,31):    # check if overflows
            return ans*s
        else:
            return 0

