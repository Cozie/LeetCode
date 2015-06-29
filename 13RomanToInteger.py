class Solution:
    # @param {string} s
    # @return {integer}

    def romanToInt(self, s):

        tot=0
        k=0

        cov={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

        for j in s:
        	tot=tot+cov[j]

        for i in range(len(s)-1,-1,-1):
        	if i<len(s)-1 and cov[(s[i])]< cov[(s[i+1])]:
        		tot=tot-2*cov[(s[i])]

        return tot
        
===============================

    def romanToInt(self, s):

        tot=0   # will get error without this line: UnboundLocalError: local variable 'tot' referenced before assignment

        cov={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

        for i in range(len(s)-1,-1,-1):
        	if i<len(s)-1 and cov[(s[i])]< cov[(s[i+1])]:
        		tot=tot-cov[(s[i])]
        	else:
        		tot=tot+cov[(s[i])]

        return tot
        
================================

    def romanToInt(self, s):
        c=[]
        tot=0
        
        for j in s:
        	if j=='M':
        		c.append(1000)
        	elif j=='D':
        		c.append(500)
        	elif j=='C':
        		c.append(100)
        	elif j=='L':
        		c.append(50)
        	elif j=='X':
        		c.append(10)
        	elif j=='V':
        		c.append(5)
        	elif j=='I':
        		c.append(1)

        for i in range(len(c)-1):
        	if c[i]<c[i+1]:
        		c[i]=-1*c[i]
        	tot=tot+c[i]
        return tot+c[-1]
