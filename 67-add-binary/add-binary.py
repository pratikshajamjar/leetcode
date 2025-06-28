class Solution:
    def addBinary(self, a: str, b: str) -> str:
        first = int(a,2)
        second = int(b,2)

        add_bin = bin(first + second)[2:]

        return add_bin
        