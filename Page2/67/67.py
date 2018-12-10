class Node:

    def __init__(self, value):
        self.value = int(value)
        self.left_node = None
        self.right_node = None

    def print(self):
        print("value = ", self.value)
        if self.left_node is None:
            print("left node is none")
            print("right node is none")
        else:
            print("left node = \n", self.left_node.to_string())
            print("right node = \n", self.right_node.to_string())

    def to_string(self):
        result = "value = " + self.value + "\n"
        if self.left_node is None:
            result += "left node = none\n"
            result += "right node = none\n"
        else:
            result += "left node: \n" + self.left_node.to_string()
            result += "right node: \n" + self.right_node.to_string()

        return result


def create_tree_from_file(file_name):

    num_lines = sum(1 for line in open(file_name, "r"))

    file = open(file_name, "r")

    tree = Node(file.readline().replace("\n", ""))

    for i in range(1, num_lines):

        old_leaves = []
        get_leaves(tree, old_leaves)
        old_leaves = remove_duplicates(old_leaves)

        new_leaves = []
        for val in file.readline().replace("\n", "").split(' '):
            new_leaves.append(Node(val))

        add_new_leaves(old_leaves, new_leaves)

    return tree


def get_leaves(tree, leaves):
    if tree.left_node is None:
        leaves.append(tree)
    else:
        get_leaves(tree.left_node, leaves)
        get_leaves(tree.right_node, leaves)


def add_new_leaves(old_leaves, new_leaves):

    for leaf in old_leaves:
        leaf.left_node = new_leaves.pop(0)
        leaf.right_node = new_leaves[0]


def remove_duplicates(l):

    i = 0

    while i < len(l) - 1:
        j = i + 1
        while j < len(l) - 1:
            if id(l[i]) == id(l[j]):
                del l[j]
            else:
                j += 1
        i += 1
    return l


def get_maximum_path(tree):

    if tree.left_node is None:
        return tree.value
    else:
        left_val = get_maximum_path(tree.left_node)
        right_val = get_maximum_path(tree.right_node)

        return tree.value + max(right_val, left_val)


t = create_tree_from_file("problem.txt")
max_path = get_maximum_path(t)
print(max_path)
