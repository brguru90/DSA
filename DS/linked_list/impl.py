import sys,os
from typing import Any
from typing import List

dir_path = os.path.dirname((os.path.dirname(os.path.realpath(__file__))))
sys.path.append(dir_path)

from my_package.console import _console as console


class LinkedListException(Exception):
    pass

class Node:
    ''' Linked list data structure '''
    def __init__(self,data) -> None:
        self.data=data
        self.next=None # used to store object reference

class LinkedList:
    ''' linked list store & method implementation '''
    def __init__(self) -> None:
        ''' initializing head node/cur_node with None'''
        self.head=None
        
    def insert_at_end(self,data) -> None:
        ''' Insert at end:
            - if there is no item in list, then just assign new node to head
            - else loop until last node(if next value of cur_node have None means its a last_node)
            - initialise data to node object & assign node object address to head(or next of last node)
        '''
        if self.head==None:
            self.head=Node(data)
        else:
            cur_node=self.head
            while cur_node.next:
                cur_node=cur_node.next
            cur_node.next=Node(data)

    def insert_at_begining(self,data) -> None:
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

    def insert_after_pos(self,pos,data) -> None:
        ''' insert at position:
            - create an temprovery node which going to be initial node
            - temprovery node has initialise with given data
            - cur_node initialized with the head/cur_node
            - loop until given position 
            - after reaching the position, create temp_node with given data
            - next of temp_node assigned with the reference of next node
              of cur_node  (like appeniding node at current position - temp_node=[new_node]+[i+1:])
            - finally next of node at current position will be assigned with
              reference of newly inserted temp_node (like updated_node=[0:i]+temp_node)
        '''

        if pos==-1:
            temp_node=Node(data)
            temp_node.next=self.head
            self.head=temp_node
            return 


        cur_node=self.head
        i=0
        while cur_node and i<pos:
            cur_node=cur_node.next
            i+=1
        temp_node=Node(data)
        if cur_node:
            temp_node.next=cur_node.next
        else:
            raise LinkedListException("Given position in list doesn't exists")
        cur_node.next=temp_node

    def replace_at_pos(self,pos,data) -> None:
        ''' replace at position:
            - while looping if the current position matches given position
            - then just replacing data
        '''
        if self.head==None:
            raise LinkedListException("List is empty")


        cur_node=self.head
        i=0
        while cur_node:
            if pos==i:
                cur_node.data=data
                break
            cur_node=cur_node.next
            i+=1

    def remove_at_beginning(self) -> Any:
        ''' remove at beggining
            replacing current head with the next head (next head's reference)
        '''
        if self.head==None:
            raise LinkedListException("List is empty")


        val=self.head.data
        self.head=self.head.next  
        return val

    def pop(self) -> Any:
        ''' removing item at the end:
            - if next of head is None(means single item in list), just replace current head with None
            - else 
            - looping until the next after next is None or (next of last 2nd node is None)
            - replacing reference of that node with None
        '''

        if self.head==None:
            raise LinkedListException("List is empty")

        if self.head.next==None:
            val=self.head.data
            self.head=None
            return val

        cur_node=self.head
        while cur_node.next and cur_node.next.next:
            cur_node=cur_node.next
        val=cur_node.next.data
        cur_node.next=None
        return val

    def remove_from_position(self,pos) -> Any:
        ''' remove from position:
            - if there is only single node, just assigning that node to None
            - else there is more than one node (means next of current node is not None)
            - then looping until reach the position
            - on reaching the position, replacing the next reference of node
             at current position  with the next of next node
        '''

        if self.head==None:
            raise LinkedListException("List is empty")
        
        val=self.head.data
        if self.head.next==None:
            self.head=None
            return val

        if pos<=0:
            val=self.head.data
            self.head=self.head.next
            return val

        cur_node=self.head
        i=0
        while cur_node and cur_node.next and i<pos-1:
            cur_node=cur_node.next
            i+=1   
        if cur_node.next: 
            val=cur_node.next.data    
            cur_node.next=cur_node.next.next   
            return val         
        else:
            raise LinkedListException("position is not exists in list")
        



    def display(self) -> None:
        if self.head==None:
            console.info("List is empty")
            return
        cur_node=self.head
        while cur_node:
            console.info(cur_node.data)
            cur_node=cur_node.next
        console.info()

    def get_elements_as_list(self) -> List[Any]:
        if self.head==None:
            return []
        arr=[]
        cur_node=self.head
        while cur_node:
            arr.append(cur_node.data)
            cur_node=cur_node.next
        return arr

if __name__ == "__main__":
    help(LinkedList)