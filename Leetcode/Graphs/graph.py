def df(head, apply=None, list_out=[]):
    """Traverse the graph depth-first, while applying the given function at each node.
       Collect the function output and store it in a list. Finally, return the list.
       
       Parameters:
        apply --> function to apply, defaults to returning the node data
        list_out --> list to return
    """
    if apply is None:
        apply = lambda x: x.data
    if head is not None:
        list_out.append(apply(head))
        df(head.left, apply, list_out)
        df(head.right, apply, list_out)
    return list_out

class GraphNode():
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return repr(self.data)


class Graph():
    def __init__(self, root=None) -> None:
        self.root = root
    
    def __repr__(self) -> str:
        return ''

    
def run_tests():
    # Create graph

    n2 = GraphNode(2)
    n3 = GraphNode(3)
    n1 = GraphNode(1, n2, n3)

    graph = Graph(n1)
    result = df(graph.root)
    print(result)
    
run_tests()