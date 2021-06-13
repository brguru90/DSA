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
        self.prev=None  # used to store object reference
class LinkedList:
    ''' linked list store & method implementation '''
    def __init__(self) -> None:
        ''' initializing head node/cur_node with None'''
        self.head=None
        # tail can be used in singly linked list, but may be while removing we can't take advantage of it
        self.tail=self.head
        
    def insert_at_end(self,data) -> None:
        ''' Insert at end:
        '''
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            temp_node=Node(data)   
            temp_node.prev=self.tail        
            self.tail.next=temp_node
            self.tail=self.tail.next
            
    def insert_at_begining(self,data) -> None:
        ''' insert at beginning:       
        '''
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
    

    def remove_at_beginning(self) -> Any:
        ''' remove at beggining
        '''
        if self.head==None:
            raise LinkedListException("List is empty")


        val=self.head.data
        self.head=self.head.next  
        if self.head:
            self.head.prev=None
        return val

    def pop(self) -> Any:
        ''' removing item at the end:
        '''

        if self.head==None:
            raise LinkedListException("List is empty")

        val = self.tail.data
        self.tail=self.tail.prev
        if self.tail:
            self.tail.next=None
        else:
            self.head=self.tail
        return val
        



    def display(self) -> None:
        if self.head==None:
            console.info("List is empty")
            return
        cur_node=self.head
        while cur_node:
            console.info(cur_node.data)
            cur_node=cur_node.next
        console.info()

    

    @property
    def as_list(self) -> List[Any]:
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