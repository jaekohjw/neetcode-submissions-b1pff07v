from collections import deque
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        cnt = 1
        hashmap = defaultdict(list)
        visited = set()
        q = deque([beginWord])
        found = False
        

        for w in wordList:
            for i in range(n):
                pattern = w[:i] + "*" + w[i+1:]
                hashmap[pattern].append(w)



        while q:
            for _ in range(len(q)):    
                word = q.popleft()

                if word == endWord:
                    return cnt
                for i in range(n):
                    pattern = word[:i] + "*" + word[i+1:]
                    for new_word in hashmap[pattern]:
                        if new_word not in visited:
                            visited.add(new_word)
                            q.append(new_word)

            cnt += 1
        
        return 0


        