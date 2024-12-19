class Solution:
    def romanToInt(self, s: str) -> int:
        # Define Roman numeral values
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        
        # Loop through the string
        for i in range(len(s)):
            # Check if the current value is less than the next value
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]  # Subtract smaller value
            else:
                total += roman_values[s[i]]  # Add current value
                
        return total
