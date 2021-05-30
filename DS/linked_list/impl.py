import sys,os

dir_path = os.path.dirname((os.path.dirname(os.path.realpath(__file__))))
sys.path.append(dir_path)

from my_package.console import _console as console

class Node:
    ''' Linked list data structure '''
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class LinkedList:
    ''' linked list store & method implementation '''
    def __init__(self) -> None:
        ''' initializing head node/cur_node with None'''
        self.head=None
        
    def insert_at_end(self,data):
        ''' initialise data to node object & assign node object address to head(or next of head) '''
        if self.head==None:
            self.head=Node(data)
        else:
            self.head.next=Node(data)

    def insert_at_begining(self,data):
        ''' insert at beginning:
            - create an temprovery node which going to be initial node
            - temprovery node has initialise with given data
            - the next of temp node is assigned with the reference of cur_node/head         
        '''
        if self.head==None:
            self.head=Node(data)
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node

    def insert_at_pos(self,pos,data):
        ''' insert at position:
            - create an temprovery node which going to be initial node
            - temprovery node has initialise with given data
            - cur_node initialized with the head/cur_node
            - loop cur_node, increment i,
            - if i matches the given position, then create temp_node with given data
            - next of temp_node assigned with the reference of next node of cur_node  (like appeniding node at current position - temp_node=[new_node]+[i+1:])
            - finally next of node at current position will be assigned with reference of newly inserted temp_node (like updated_node=[0:i]+temp_node)
        '''
        cur_node=self.head
        i=0
        while cur_node:
            if pos==i:
                temp_node=Node(data)
                temp_node.next=cur_node.next
                cur_node.next=temp_node
                break
            cur_node=cur_node.next
            i+=1

    def replace_at_pos(self,pos,data):
        cur_node=self.head
        i=0
        while cur_node:
            if pos==i:
                cur_node.data=data
                break
            cur_node=cur_node.next
            i+=1


    def display(self):
        cur_node=self.head
        while cur_node:
            console.info(cur_node.data)
            cur_node=cur_node.next
        console.info()

ll=LinkedList()


ll.insert_at_end(1)
ll.insert_at_end(2)
ll.display()


ll.insert_at_begining(-1)
ll.insert_at_begining(-2)
ll.display()

ll.insert_at_pos(2,1.5)
ll.display()

ll.insert_at_pos(2,1.4)
ll.display()

ll.replace_at_pos(3,1.2)
ll.replace_at_pos(4,1.4)
ll.display()

