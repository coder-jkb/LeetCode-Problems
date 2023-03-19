class Trie:
    def __init__(self):
        self.points = dict()
        self.end = False
        
class WordDictionary:

    def __init__(self):
        self.start = Trie()

    def addWord(self, word: str) -> None:
        node = self.start
        for ch in word:
            if ch not in node.points:
                node.points[ch] = Trie()
            node = node.points[ch]
        node.end = True

    def search(self, word: str) -> bool:
        
        def DFS(start_inx, root):
            node = root
            for i in range(start_inx, len(word)):
                ch = word[i]
                if ch == '.':
                    for child in node.points.values():
                        if DFS(i+1, child):
                            return True
                    return False

                else:
                    if ch not in node.points:
                        return False
                    
                    node = node.points[ch]

            return node.end
        
        return DFS(0, self.start)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)