class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        ten = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        more = ['Thousand','Million', 'Billion']
        def word(num):
        	if num<=19:
        		return dic[num-1:num]
        	if num<100:
        		return [ten[num/10-2]]+ word(num%10)
        	if num<1000:
        		return [dic[num/100 - 1], 'Hundred'] + word(num%100)
    		for p in range(3):
    			if num < 1000**(p+2):
    				return word(num/(1000**(p+1))) + [more[p]] + word(num%(1000**(p+1)))

    	# print word(num)
    	return ' '.join(word(num)) or 'Zero'

print Solution().numberToWords(1500000000)