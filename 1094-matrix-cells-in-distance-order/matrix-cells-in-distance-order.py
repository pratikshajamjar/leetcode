class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int):
        result = []

        for r in range(rows):
            for c in range(cols):
                dist = abs(r - rCenter) + abs(c - cCenter)
                result.append((dist, [r, c]))

        # Sort by distance
        result.sort()

        # Extract just the coordinates
        return [cell for dist, cell in result]
