from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        pre_req_dict = {}
        for pre_req in prerequisites:
            entry = pre_req_dict.get(pre_req[0], set())
            entry.add(pre_req[1])
            pre_req_dict[pre_req[0]] = entry

        ans = []
        cycle_exists = False
        processed = set()
        def dfs(course, traversal_count):

            # cycle detected
            if traversal_count > numCourses:
                nonlocal cycle_exists
                cycle_exists = True
                return

            # processed
            if course in processed:
                return

            # traverse
            if course in pre_req_dict:
                for pre_req in pre_req_dict[course]:
                    dfs(pre_req, traversal_count + 1)

            ans.append(course)
            processed.add(course)

        to_traverse = set()
        all_courses = set()
        for reqs in prerequisites:
            for course in reqs:
                all_courses.add(course)
        for course in range(numCourses):
            if course not in all_courses:
                ans.append(course)
            else:
                to_traverse.add(course)
        for course in to_traverse:
            dfs(course, 1)

        if cycle_exists:
            return []
        else:
            return ans

def main():
    sol = Solution()
    #         2 -> 0 -> 3 -> 4
    #              ^    ^
    #              1    5
    # print(sol.findOrder(6,[[2,0],[1,0],[0,3],[3,4],[3,5]]))
    # print(sol.findOrder(2, []))
    # print(sol.findOrder(3, [[1,0]]))
    print(sol.findOrder(4,[[3,0],[0,1]]))

if __name__ == "__main__":
    main()