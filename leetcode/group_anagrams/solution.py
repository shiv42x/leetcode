class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        """
        key: val
        a hashmap where the key is a sorted tuple of a word's letters 
        and val is an array with members of that group
        """

        letter_map = defaultdict(list)

        for word in strs:
            letters = tuple(sorted(word))
            letter_map[letters].append(word)

        return list(letter_map.values())