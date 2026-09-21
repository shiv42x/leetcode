class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbours = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                neighbours[pattern].append(word)
        
        visited = set([beginWord])
        queue = deque([beginWord])
        length = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return length
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for neighbourWord in neighbours[pattern]:
                        if neighbourWord not in visited:
                            visited.add(neighbourWord)
                            queue.append(neighbourWord)

            length += 1
        return 0