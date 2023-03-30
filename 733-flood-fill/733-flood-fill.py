class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(sv):
            a,b=sv[0],sv[1]
            image[a][b]=color
            if b>0 and image[a][b-1]==og: #left
                image[a][b-1]=color
                dfs([a,b-1])
            if b<n-1 and image[a][b+1]==og: #right
                image[a][b+1]=color
                dfs([a,b+1])
            if a>0 and image[a-1][b]==og: #up
                image[a-1][b]=color
                dfs([a-1,b])
            if a<m-1 and image[a+1][b]==og: #down
                image[a+1][b]=color
                dfs([a+1,b])
        m=len(image)
        n=len(image[0])
        og=image[sr][sc]
        if og==color:
            return image
        dfs([sr,sc])
        return image
        