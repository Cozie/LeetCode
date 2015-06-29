class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        pre=''
        p=''
        j=0
        k=0
        T=True

        if len(strs)==0:
            T=False
            short=''
        else:
            short= strs[0]

        for i in strs:
        	if len(i)< len(short):
        		short=i

#        print short

        for k in range(0,len(short)):
        	p=''
        	if T==False:
        		break
        	while (j<len(strs)):
        		if strs[j][k]!=short[k]:
        			p=''
        			T=False
        			break
        		p=short[k]
        		j=j+1
        	pre=pre+p
        	j=0
        	k=k+1
        
        return pre

#        print 'pre=', pre
        
