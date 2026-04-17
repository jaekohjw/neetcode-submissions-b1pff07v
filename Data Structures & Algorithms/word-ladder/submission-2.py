from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        hashmap = defaultdict(list)
        
        # 1. Build the adjacency list using wildcard patterns
        for w in wordList:
            for i in range(n):
                pattern = w[:i] + "*" + w[i+1:]
                hashmap[pattern].append(w)

        # 2. Initialize BFS components
        q = deque([beginWord])
        visited = {beginWord}  # Initialize with the starting word
        cnt = 1

        # 3. Perform Level-Order BFS
        while q:
            # Process all words at the current level
            for _ in range(len(q)):    
                word = q.popleft()

                # If we reach the target, return the current sequence length
                if word == endWord:
                    return cnt
                
                # Generate patterns for the current word to find neighbors
                for i in range(n):
                    pattern = word[:i] + "*" + word[i+1:]
                    
                    for new_word in hashmap[pattern]:
                        if new_word not in visited:
                            visited.add(new_word)  # Mark as visited IMMEDIATELY
                            q.append(new_word)

            # Increment sequence length after completing a full level
            cnt += 1
        
        return 0