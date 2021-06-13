import sys,os
dir_path = os.path.dirname(os.path.dirname((os.path.dirname(os.path.realpath(__file__)))))
sys.path.append(dir_path)

from DS.doubly_linked_list.impl import LinkedList,LinkedListException
from DS.my_package.console import _console as console




ll=LinkedList()


ll.insert_at_end(1)
ll.insert_at_end(2)
ll.display()


ll.insert_at_begining(-1)
ll.insert_at_begining(-2)
ll.display()



ll.insert_at_begining(-3)
ll.insert_at_end(3)
ll.insert_at_begining(-4)
ll.insert_at_end(4)
ll.display()


ll.remove_at_beginning()
ll.display()

ll.pop()
ll.pop()
ll.display()


ll.remove_at_beginning()
ll.remove_at_beginning()
ll.remove_at_beginning()
ll.display()

ll.pop()
ll.pop()
ll.display()


ll.insert_at_end(1)
ll.insert_at_end(2)
ll.display()


ll.remove_at_beginning()
ll.remove_at_beginning()
ll.display()