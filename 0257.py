## 2020/06/30
from typing import List

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        self.res = []
        self.dfs(root, [str(root.val)])
        return self.res

    def dfs(self, root, path):
        if not root.left and not root.right:
            self.res.append('->'.join(path))
        if root.left:
            self.dfs(root.left, path + [str(root.left.val)])
        if root.right:
            self.dfs(root.right, path + [str(root.right.val)])