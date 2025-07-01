class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        # Find mismatched characters
        mismatches = []
        for a, b in zip(s1, s2):
            if a != b:
                mismatches.append((a, b))

        # Check if there are exactly 2 mismatches and they can be swapped
        return len(mismatches) == 2 and mismatches[0] == mismatches[1][::-1]
