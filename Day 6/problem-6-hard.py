class Node:
    def __int__(self, data):
        self._data = data
        self._both = None


class LikedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._list = []


    def get(self, node_id):
        pass

    def add(self, data):
        node = Node(data)

        if self._head is None:
            self._head = node
            self._list = node
        else:
            pass
