import sys,os,time
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
        
    def insert_at_end(self,data) -> None:
        ''' Insert at end:
        '''
        if self.head==None:
            self.head=Node(data)
            self.head.next=self.head
            self.head.prev=self.head
        else:
            temp_node=Node(data)   
            # modify head first
            last_node=self.head.prev
            self.head.prev=temp_node
            # after link newly modified head
            last_node.next=temp_node
            temp_node.next=self.head
            temp_node.prev=last_node
            
    def insert_at_begining(self,data) -> None:
        ''' insert at beginning:       
        '''
        if self.head==None:
            self.head=Node(data)
            self.head.next=self.head
            self.head.prev=self.head
        else:
            new_front_node=Node(data)
            # modify head first
            last_node=self.head.prev
            last_node.next=new_front_node
            self.head.prev=new_front_node
            # after link newly modified head
            new_front_node.next=self.head
            new_front_node.prev=last_node
            self.head=new_front_node
    

    def remove_at_beginning(self) -> Any:
        ''' remove at beggining
        '''
        if self.head==None:
            raise LinkedListException("List is empty - remove_at_beginning")
    
        if id(self.head.next)==id(self.head):
            self.head=None
            return

        val=self.head.data
        last_node=self.head.prev
        # removing first node
        self.head=self.head.next  
        last_node.next=self.head
        self.head.prev=last_node
        
        return val

    def pop(self) -> Any:
        ''' removing item at the end:
        '''

        if self.head==None:
            raise LinkedListException("List is empty - pop")


        if id(self.head.next)==id(self.head):
            self.head=None
            return

        val = self.head.prev.data
        prev_1=self.head.prev.prev
        prev_1.next=self.head
        self.head.prev=prev_1        
        return val
        



    def display(self) -> None:
        if self.head==None:
            console.info("List is empty - display")
            return
        cur_node=self.head
        console.info(cur_node.data)
        # print("prev",cur_node.prev.data)
        # print("next",cur_node.next.data)
        cur_node=cur_node.next
        while id(cur_node)!=id(self.head):
            console.info(cur_node.data)
            # print("prev",cur_node.prev.data)
            # print("next",cur_node.next.data)
            cur_node=cur_node.next
            # time.sleep(1)
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