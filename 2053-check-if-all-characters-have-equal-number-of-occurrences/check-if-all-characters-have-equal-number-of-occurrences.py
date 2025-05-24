class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hash_map=Counter(s)
        for value in hash_map.values():
            if value!=hash_map[s[0]]:
                return False
        return True