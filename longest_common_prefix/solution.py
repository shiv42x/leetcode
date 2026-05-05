class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        can use trie instead.
            populate trie from input strings
            build result until you encounter a node with children

        class TrieNode:
            def __init__(self, char='', end=False, children=[])
                self.char = char
                self.end = end
                self.children = children
        
        """
        result = ""
        shortest_word = ""

        for string in strs:
            if shortest_word == "" and string != "":
                shortest_word = string
            elif len(string) < len(shortest_word):
                shortest_word = string
        print(shortest_word)
        for string in strs:
            i = 0
            n = len(shortest_word)
            while shortest_word not in string[0:n - i]:
                shortest_word = shortest_word[0:-1]
                i += 1
            result = shortest_word