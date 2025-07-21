class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Each element will be [char, count]
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()  # Remove the group
            else:
                stack.append([char, 1])  # New character with count 1
        
        # Reconstruct the final string
        result = ''.join(char * count for char, count in stack)
        return result
