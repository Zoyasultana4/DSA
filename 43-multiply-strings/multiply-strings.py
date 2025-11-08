class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        len1, len2 = len(num1), len(num2) 
        result = [0] * (len1 + len2)
        for i in range(len1 - 1, -1, -1):
            digit1 = int(num1[i])
          
            for j in range(len2 - 1, -1, -1):
                digit2 = int(num2[j])
                result[i + j + 1] += digit1 * digit2
        for i in range(len1 + len2 - 1, 0, -1):
            result[i - 1] += result[i] // 10
            
            result[i] %= 10
        start_index = 0 if result[0] != 0 else 1
        return "".join(str(digit) for digit in result[start_index:])