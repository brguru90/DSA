import numpy as np
import sys,os,json

dir_path = os.path.dirname((os.path.dirname(os.path.realpath(__file__))))
sys.path.append(dir_path)


from my_package.console import _console as console

class StackImpl:
    "simple stack implementation using numpy array"

    stack_size=5
    top=-1
    arr=None

    def declare_arr(self):
        self.arr=np.zeros(shape=(self.stack_size),dtype=np.int16)

    def __init__(self,stack_size) -> None:
        ''' Set the stack_size,set stack position to beggining,initialise empty zeros to all indexes  '''
        self.stack_size=stack_size
        self.top=-1
        self.declare_arr()


    def push(self,val) -> None:
        ''' push new item into top of stack '''
        if self.top==self.stack_size-1:
            raise Exception("stack overflow!")
            return
        self.top+=1
        self.arr[self.top]=val

    def pop(self,pos=None) -> int:
        ''' remove an item from top of stack '''

        if pos:
            return self.remove_at(pos)


        if self.top<0:
            raise Exception("stack empty")
        val=self.arr[self.top]
        self.arr[self.top]=0
        self.top-=1
        return val

    def remove_at(self,pos) -> int:
        if pos>self.top:
            raise Exception("index out of boundary")
        val=self.arr[pos]
        self.arr=np.concatenate((self.arr[0:pos],self.arr[pos+1:]))
        self.top-=1
        return val

    def space_available(self) -> int:
        ''' returns the avaliable space in stack '''
        return self.stack_size-self.top

    def display(self) -> None:
        ''' displays all values inside stack ''' 
        for i in range(self.top+1):
            console.info(self.arr[i])

    def get_values(self) -> None:
        ''' get array ''' 
        return self.arr[0:self.top]

    def to_python_type(self,val):
        if isinstance(val,np.int16):
            return int(val)
        else:
            return val

    def __str__(self) -> str:
        ''' shows the all the member of class in json string '''
        data={
            "top":self.top,
            "stack_size":self.stack_size,
            "stack_data":[_item for _item in self.arr]
        }
        return json.dumps(data,indent=2,default=self.to_python_type)





if __name__ == "__main__":
    help(StackImpl)




        