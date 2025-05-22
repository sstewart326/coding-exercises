# time for search - O(n) for no wildcards. O(26^W * N) where W is wild cards as we can have 26 possible characters per wildcard
# space - O(n) total num of characters across all words
class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie

        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]

        node['$'] = {}

    def search(self, word: str) -> bool:

        def traverse(word, node):
            if len(word) == 1:
                return '$' in node
            head = word[0]
            if head in node:
                return traverse(word[1:], node[head])
            elif head == ".":
                matched = False
                for child in node.values():
                    if child and traverse(word[1:], child):
                        matched = True
                return matched
            else:
                return False

        return traverse(word + "$", self.trie)

def main():
    dict = WordDictionary()
    dict.addWord("at")
    dict.addWord("and")
    dict.addWord("an")
    dict.addWord("add")
    print(dict.search("a"))


if __name__ == "__main__":
    main()