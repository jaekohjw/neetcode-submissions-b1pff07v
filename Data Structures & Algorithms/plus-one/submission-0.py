class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ret = ""
        res = []
        for i in range(len(digits) - 1, -1, -1):
            sum = digits[i] + carry
            if sum >= 10:
                carry = sum // 10
            else:
                carry = 0
            ret = str(sum % 10) + ret
                
        if carry != 0:
            ret = str(carry) + ret
        
        for c in ret:
            res.append(c)
        return res
        