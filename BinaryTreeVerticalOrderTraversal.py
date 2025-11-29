# The time complexity: O(n), traversing through all the elements. Space complexity: O(n) as well for the queue

# The intuition here is to determine the index for every column, for that we start with 0 index and then from then on for left subtree we subtract 1 and for right subtree we add 1.
# This way we are able to get the same index for all the columns. We also keep track of min and max value which we can iterate later through the hashmap and put it in our result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque()
        queue.append((0, root))
        hashmap = defaultdict(list)
        minVal = float("inf")
        maxVal = float("-inf")
        while queue:
            for _ in range(len(queue)):
                idx, node = queue.popleft()
                minVal = min(idx, minVal)
                maxVal = max(idx, maxVal)
                hashmap[idx].append(node.val)
                if node.left:
                    queue.append((idx - 1, node.left))

                if node.right:
                    queue.append((idx + 1, node.right))
        result = []
        for i in range(minVal, maxVal + 1):
            result.append(hashmap[i])

        return result

