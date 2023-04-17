#include <stdio.h>

class LinkedList{
    public:
        LinkedList();
        Node * head;
        void append(Node);
};

LinkedList::LinkedList(){
    head = NULL;
}

void LinkedList::append(Node * node){
    node->next = head;
    head = node;
}

class Node{
    public:
        Node(int);
        int data;
        Node * next;
};

Node::Node(int x){
    data = x;
    next = NULL;
}




int main() {

    LinkedList list1 = LinkedList();
    LinkedList list2 = LinkedList();

    //
    Node node0 = Node(1);
    Node node1 = Node(11);
    Node node2 = Node(5);
    Node node3 = Node(7);

    list1.append(node0);
    list2.append(node2);

    return 0;
}