class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i:[] for i in range(numCourses)}
        result = []

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        # 0 = unvisited, 1 = visiting, 2 = visited
        states = [0] * numCourses
        def dfs(course):
            if states[course] == 1:
                return False
            
            elif states[course] == 2:
                return True

            states[course] = 1
            
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False

            states[course] = 2
            result.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return result 