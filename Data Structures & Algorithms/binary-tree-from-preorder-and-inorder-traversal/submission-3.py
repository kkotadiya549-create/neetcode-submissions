class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {value: i for i, value in enumerate(inorder)}

        pre_index = 0

        def build(left, right):
            nonlocal pre_index

            if left > right:
                return None

            root_value = preorder[pre_index]
            pre_index += 1

            root = TreeNode(root_value)

            mid = inorder_map[root_value]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)