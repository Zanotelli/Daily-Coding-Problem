def serialize(root):
    left = ""
    right = ""
    if root.left is not None:
        left = serialize(root.left)
    if root.right is not None:
        right = serialize(root.right)
    return f"{root.val}:[{left},{right}]"


def get_matching_parenthesis(string):
    stack = []
    if "[" in string:
        for i in range(len(string)):
            if string[i] == "[":
                stack.append(i)
            elif string[i] == "]":
                aux = stack.pop()
                if stack.__len__() == 0:
                    return [aux+1, i]


def deserialize(root):
    if root != "":
        val = None
        if ":" in root:
            val = root[:(root.find(":"))]

        par = get_matching_parenthesis(root)
        sub_root = root[par[0]: par[1]]

        sub_root_l = ""
        sub_root_r = ""

        div = None
        if sub_root != ",":
            div = get_matching_parenthesis(sub_root)[1]

        if div is not None:
            sub_root_l = sub_root[:(div+1)]
            sub_root_r = sub_root[(div+2):]

        left = None
        right = None

        if sub_root_l != "" and sub_root_l[0] != ",":
            left = deserialize(sub_root_l)
        if sub_root_r != "":
            right = deserialize(sub_root_r)

        return Node(val, left, right)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'