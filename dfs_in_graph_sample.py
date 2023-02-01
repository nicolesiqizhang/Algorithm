class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class GraphNode:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def add_neighbor_list(self, node_list: list):
        for node in node_list:
            self.neighbors.append(node)

    def __str__(self):
        str_info = "node:" + str(self.id) + " with neighbors: "
        for n in self.neighbors:
            str_info += str(n.id) + ","
        return str_info


def travel(node, visited):
    visited.append(node.id)
    # ////...;;';';'l,#?'

    for neighbor in node.neighbors:
        if neighbor.id not in visited:
            travel(neighbor, visited)

def process_list(l: list, new_value):
    success = False
    if new_value not in l:
        l.append(new_value)
        success = True
    return success

def findmax(l):
    if l is None or len(l) == 0:
        return 0

    current_max = l[0]
    # for num in l:
    #     if num > current_max:
    #         current_max = num
    index = 0
    while index < len(l):
        if l[index] > current_max:
            current_max = l[index]
    return current_max


def find_max_tree(root: TreeNode) -> int:
    current_max_node = root
    while current_max_node.right is not None:
        current_max_node = current_max_node.right

    return current_max_node.val

def main():
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    node5 = GraphNode(5)
    node6 = GraphNode(6)
    node7 = GraphNode(7)
    node8 = GraphNode(8)

    node1.add_neighbor_list([node2, node3])
    node2.add_neighbor_list([node1, node4, node7])
    node3.add_neighbor_list([node1, node4, node6])
    node4.add_neighbor_list([node2, node3, node5, node7])
    node5.add_neighbor_list([node4, node6])
    node6.add_neighbor_list([node3, node5, node8])
    node7.add_neighbor_list([node2, node7])
    node8.add_neighbor_list([node6])

    # visited = []
    # travel(node1, visited)
    # print(visited)

    l = None
    print(findmax(l))
    # print("before process:", l)
    # print(process_list(l, 5))
    # print("before process 1:", l)
    # print(process_list(l, 5))
    # print("before process 2:", l)


main()