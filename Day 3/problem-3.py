def serialize(root):
    left = ""
    right = ""
    if root.left is not None:
        left = serialize(root.left)
    if root.right is not None:
        right = serialize(root.right)
    return f"{root.val}:[{left},{right}]"


# def deserialize(root):
#     if root != "":
#         val = root[:(root.find(":"))]
#         sub_root = root[root.find("[")+1: root.rfind("]")]
#         print(sub_root)
#
#         left = None
#         right = None
#         if sub_root.index(0) != ",":
#             left = deserialize(sub_root)
#         else:
#             right = deserialize(sub_root[1:])
#
#
#         left = root[root.find("l.")+1: root.find(",r.")]
#         right = root[root.find("r.")+1:]
#         print(left)
#         print(right)
#
#         return Node(val, left, right)
def deserialize(root):
    if root != "":
        val = root[:(root.find(":"))]
        sub_root = root[root.find("[")+1: root.rfind("]")]
        print(sub_root)

        left = None
        right = None


        return Node(val, left, right)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'