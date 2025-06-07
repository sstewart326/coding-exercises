from typing import List


class Solution:

    # time - O(A*E) where a is the number of accounts and e is the average emails per account
    # space - O(V + E) where v is the emails and e is the connection to related emails
    def build_graph(self, accounts):
        graph = {}

        for account in accounts:
            emails = account[1:]
            # Add the first email (if any)
            if emails:
                if emails[0] not in graph:
                    graph[emails[0]] = set()

                # Connect all emails in this account
                for j in range(1, len(emails)):
                    # Add bidirectional edges between first email and all others
                    graph[emails[0]].add(emails[j])

                    if emails[j] not in graph:
                        graph[emails[j]] = set()
                    graph[emails[j]].add(emails[0])

        return graph

    # time - O(e) where e is the edges of the email
    # space - O(v) where v is the visited
    def dfs(self, graph, email, visited):
        if email in visited:
            return []
        visited.add(email)

        graphed_emails = graph[email]

        emails_to_return = [email]
        for e in graphed_emails:
            emails_to_return += self.dfs(graph, e, visited)

        return emails_to_return

    # 1. Build the graph
    # create empty adjacency list (graph)
    # create email-to-name map

    # 2. Use DFS to find connected components
    # create empty visited set
    # create empty result list

    # 3. Find all connected components
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = self.build_graph(accounts)

        visited = set()
        ans = []
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                account_emails = self.dfs(graph, email, visited)
                if account_emails:
                    sorted_emails = sorted(account_emails)
                    sorted_emails.insert(0, name)
                    ans.append(sorted_emails)

        return ans


# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

def main():
    sol = Solution()
    input = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    print(sol.accountsMerge(input))

if __name__ == "__main__":
    main()