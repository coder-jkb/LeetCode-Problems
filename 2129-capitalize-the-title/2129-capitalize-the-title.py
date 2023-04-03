class Solution:
    def capitalizeTitle(self, title: str) -> str:
        sentence = title.lower().split(" ")
        ans = []
        for word in sentence:
            if len(word) > 2:
                ans.append(word[0].upper()+word[1:])
            else:
                ans.append(word)
            
        return " ".join(ans)