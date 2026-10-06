from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        children = defaultdict(list)

        for course, prereq in prerequisites:
            children[prereq].append(course)
            indegree[course] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        res = []
        while q:
            v = q.popleft()
            res.append(v)
            for c in children[v]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        return len(res) == numCourses
        
        