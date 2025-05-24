class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        process = []
        for j in range(1, area + 1):
            if area % j == 0: 
                pair = [j, area // j]
                if pair not in process:  
                    process.append(pair)
        min_value = [area, 1]
        for e in range(len(process)):
            L, W = process[e]
            if L >= W and (sum(process[e])< sum(min_value)):  
                min_value = [L, W]
        return min_value
        