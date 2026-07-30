class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list)

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        states = [0] * numCourses
        def dfs(course):
            if states[course] == 1:
                return False
            
            if states[course] == 2:
                return True

            states[course] = 1
            for prereq in prereq_map[course]:
                if not dfs(prereq): return False
    
            states[course] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True
View less
 
