class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def get(node):
            return [i for i in [node.left,node.right] if i]
        if not root:
            return []
        level = [root]
        while level:
            ans.append([i.val for i in level])
            temp = []
            for nd in level:
                temp += get(nd)
            level = temp
        return ans[::-1]