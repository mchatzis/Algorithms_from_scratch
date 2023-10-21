from binary_tree import Tree, TreeNode


def test_TreeNode_eq():
    emptyNode = TreeNode()
    assert emptyNode == TreeNode(None, None, None)
    assert emptyNode == TreeNode(None, TreeNode(5,None,None), None)

    leafA = TreeNode(3, None, None)
    leafB = TreeNode(5, None, None)
    root = TreeNode(5, leafA, leafB)
    rootB = TreeNode(2, leafA, leafB)
    assert leafA != leafB
    assert leafA != root
    assert leafB == root
    assert rootB != root

def test_Tree_eq():
    emptyTree = Tree()
    assert emptyTree == Tree(root=None)

    leafA = TreeNode(3, None, None)
    leafB = TreeNode(7, None, None)
    root = TreeNode(5, leafA, leafB)
    tree = Tree(root)
    treeB = Tree(lst=[7,3,5])
    assert tree == treeB, f"Tree A:\n{tree.toListBf()} \n is not equal to TreeB: \n {treeB.toListBf()}"

def test_Tree_str():
    emptyTree = Tree()
    assert str(emptyTree) == ""
    
    leafA = TreeNode(3, None, None)
    leafB = TreeNode(7, None, None)
    root = TreeNode(5, leafA, leafB)
    tree = Tree(root)

    assert str(tree) == "[5, 3, 7, None, None, None, None]"

def test_buildBSTfromSortedList():
    assert Tree().buildBSTfromSortedList([]) == Tree()
    test_case = [-65, -64, -55, -50, -43, -30, -10, 0, 5, 10, 11, 34, 56, 70, 74]
    pass

def test_toList():
    assert Tree().toListBf() == []
    test_case = [-65, -64, -55, -50, -43, -30, -10, 0, 5, 10, 11, 34, 56, 70, 74]
    tree = Tree(lst=test_case)




