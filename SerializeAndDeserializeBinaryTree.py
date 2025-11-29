# Time complexity is O(n) using DFS approach to get string value during serialization. Space is O(n) as well for recursion depth

# The logic is to use a dfs to serialize and then use dfs again to deserialize. This can be done using BFS approach as well shown below

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serializeDFS(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        strList = []
        self.serializeHelper(root, strList)
        return "".join(strList)

    def serializeHelper(self, root, strList):

        if root == None:
            strList.append("#")
            strList.append(",")
            return
        strList.append(str(root.val))
        strList.append(",")
        self.serializeHelper(root.left, strList)
        self.serializeHelper(root.right, strList)

    def deserializeDFS(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "": return None
        dataArr = data.split(",")
        self.idx = 0

        def dfs():

            if dataArr[self.idx] == "#":
                self.idx += 1
                return None

            # left
            root = TreeNode(int(dataArr[self.idx]))
            self.idx += 1
            root.left = dfs()

            root.right = dfs()

            return root

        return dfs()


#BFS approach. The space and time complexity is the same
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        strVal = ""
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node == "#":
                strVal += node + ","
                continue
            if node is not None:
                strVal += str(node.val) + ","
                if node.left is None:
                    queue.append("#")
                else:
                    queue.append(node.left)

                if node.right is None:
                    queue.append("#")
                else:
                    queue.append(node.right)

        print(strVal)
        return strVal

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "": return None
        dataArr = data.split(",")
        idx = 0
        queue = deque()
        root = TreeNode(int(dataArr[0]))
        queue.append(root)
        idx += 1
        while queue and idx < len(dataArr):
            curr = queue.popleft()
            if dataArr[idx] == "#":
                curr.left = None
                idx += 1
            else:
                curr.left = TreeNode(int(dataArr[idx]))
                queue.append(curr.left)
                idx += 1

            if dataArr[idx] == "#":
                curr.right = None
                idx += 1
            else:
                curr.right = TreeNode(int(dataArr[idx]))
                queue.append(curr.right)
                idx += 1
        return root

