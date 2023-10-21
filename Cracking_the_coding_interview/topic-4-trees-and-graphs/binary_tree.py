from collections import deque

class TreeNode():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.value)
    def __eq__(self, __value:object) -> bool:
        # Two nodes are equal if the store the same value
        # i.e. their child nodes do not matter
        if not isinstance(__value, TreeNode):
            return False
        return self.value == __value.value

class Tree():
    def __init__(self, root=None, lst=None) -> None:
        if lst is not None:
            lst = sorted(lst)
            if lst == []:
                self.root = TreeNode()
            else:
                self.root = self.buildBSTfromSortedList(lst)
            return
        self.root = root

    def __str__(self):
        if self.root == None:
            return ""
        q = deque()
        q.appendleft(self.root)
        lst = self._toListBf(q)
        return str(lst)

    def toListBf(self):
        if self.root == None:
            return []
        q = deque()
        q.appendleft(self.root)
        return self._toListBf(q)

    def _toListBf(self, q, lst=[]):
        if len(q) == 0:
            return lst
        node = q.pop()
        if node is None:
            lst.append(None)
            return self._toListBf(q, lst)
        lst.append(node.value)
        q.appendleft(node.left)
        q.appendleft(node.right)
        return self._toListBf(q, lst)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Tree):
            return False
        return self._eq(self.root, __value.root)
        
    def _eq(self, nodeA, nodeB):
        if nodeA is None and nodeB is None:
            return True
        return nodeA == nodeB and self._eq(nodeA.left, nodeB.left) and self._eq(nodeA.right, nodeB.right)
        
    def buildBSTfromSortedList(self, lst):
        if lst == []:
            return Tree()
        return self._buildFromList(lst)

    def _buildFromList(self, lst):
            if lst == []:
                return None
            mid = len(lst)//2
            return TreeNode(lst[mid],self._buildFromList(lst[:mid]), self._buildFromList(lst[mid+1:]))
    



