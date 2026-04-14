class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        # Keep looping as long as n is not 1 and we haven't seen n before
        while n != 1 and n not in seen:
            seen.add(n)
            
            # Calculate the sum of squares of the current n
            current_sum = 0
            for digit in str(n):
                current_sum += int(digit) ** 2
                
            # Update n to the new sum for the next iteration
            n = current_sum
            
        # If the loop exited because n became 1, it's non-cyclical (Happy)
        return n == 1