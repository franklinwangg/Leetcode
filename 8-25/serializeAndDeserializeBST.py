from collections import deque

class Codec:
    def serialize(self, root):
        if not root:
            return "null"

        q = deque([root])
        res = []

        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")

        return ",".join(res)

    def deserialize(self, data):
        arr = data.split(",")
        if arr[0] == "null":
            return None

        root = TreeNode(int(arr[0]))
        q = deque([root])
        i = 1

        while q and i < len(arr):
            node = q.popleft()

            if arr[i] != "null":
                node.left = TreeNode(int(arr[i]))
                q.append(node.left)
            i += 1

            if i < len(arr) and arr[i] != "null":
                node.right = TreeNode(int(arr[i]))
                q.append(node.right)
            i += 1

        return root
