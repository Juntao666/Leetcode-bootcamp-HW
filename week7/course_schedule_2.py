class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}
        for course in range(numCourses):
            prereq[course] = []
        for course, pre in prerequisites:
            prereq[course].append(pre)
        
        visited = set()
        visiting = set()
        res = []

        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False
            res.append(course)
            visiting.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return res