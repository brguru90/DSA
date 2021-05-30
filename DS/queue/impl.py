import numpy as np
import sys,os,json

dir_path = os.path.dirname((os.path.dirname(os.path.realpath(__file__))))
sys.path.append(dir_path)




from my_package.console import _console as console

class QueueImpl:
    "simple Queue implementation using numpy array"

    queue_size=5
    pos=-1
    arr=None

    def declare_arr(self):
        self.arr=np.zeros(shape=(self.queue_size),dtype=np.int16)

    def __init__(self,queue_size) -> None:
        ''' Set the queue_size,set queue position to beggining,initialise empty zeros to all indexes  '''
        self.queue_size=queue_size
        self.pos=-1
        self.declare_arr()


    # @property
    # def cur_pos(self) -> int:
    #     return (self.queue_size-1)-self.pos

    # @cur_pos.setter
    # def cur_pos(self,pos_val) -> None:
    #     self.pos=(self.queue_size-1)-pos_val



    def insert(self,val) -> None:
        ''' int new item into beggining of queue '''
        if self.pos>=self.queue_size-1:
            raise Exception("queue overflow!")
            return
        self.pos+=1
        self.arr[self.pos]=val

    def remove(self,pos=None) -> int:
        ''' remove an item from queue '''
        if pos:
            return self.remove_at(pos)
        if self.pos<0:
            raise Exception("Queue empty")

        return self.remove_at(0)

    def remove_at(self,pos) -> int:
        if pos>self.pos:
            raise Exception("index out of boundary")
        val=self.arr[pos]
        self.arr=np.concatenate((self.arr[0:pos],self.arr[pos+1:]))
        self.arr=np.concatenate((self.arr,np.zeros(shape=(1),dtype=np.int16)))
        self.pos-=1
        return val

    def space_available(self) -> int:
        ''' returns the avaliable space in Queue '''
        return self.queue_size-self.pos

    def display(self) -> None:
        ''' displays all values inside Queue ''' 
        for i in range(self.pos+1):
            console.info(self.arr[i])

    def get_values(self) -> None:
        ''' get array ''' 
        return self.arr[0:self.pos+1]

    def to_python_type(self,val):
        if isinstance(val,np.int16):
            return int(val)
        else:
            return val

    def __str__(self) -> str:
        ''' shows the all the member of class in json string '''
        data={
            "pos":self.pos,
            "queue_size":self.queue_size,
            "queue_data":[_item for _item in self.arr]
        }
        return json.dumps(data,indent=2,default=self.to_python_type)

    def free(self):
        self.pos=-1
        self.arr=np.empty(0,dtype=np.int16)




if __name__ == "__main__":
    help(QueueImpl)




        