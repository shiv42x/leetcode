class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # idx: (min, max)
        # init with (n + 1) elements because buildings start from 1, 0th element will be unused
        # rows will store the min and max columns for that row
        rows = [((n + 1), 0)] * (n + 1)
        # cols will store the min and max rows for that col
        cols = [((n + 1), 0)] * (n + 1)

        num_covered_buildings = 0
   
        for building_x, building_y in buildings:
            min_y, max_y = rows[building_x]
            min_x, max_x = cols[building_y]

            rows[building_x] = (min(min_y, building_y), max(max_y, building_y))
            cols[building_y] = (min(min_x, building_x), max(max_x, building_x))

        for building_x, building_y in buildings:
            min_y, max_y = rows[building_x]
            min_x, max_x = cols[building_y]

            if (building_x < max_x) and (building_x > min_x) and (building_y < max_y) and (building_y > min_y):
                num_covered_buildings += 1
                
        return num_covered_buildings