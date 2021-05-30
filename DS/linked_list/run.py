import sys,os
dir_path = os.path.dirname(os.path.dirname((os.path.dirname(os.path.realpath(__file__)))))
sys.path.append(dir_path)

from DS.linked_list.impl import LinkedList,LinkedListException
from DS.my_package.console import _console as console




ll=LinkedList()


ll.insert_at_end(1)
ll.insert_at_end(2)
ll.display()


ll.insert_at_begining(-1)
ll.insert_at_begining(-2)
ll.display()

ll.insert_after_pos(2,1.5)
ll.display()

ll.insert_after_pos(2,1.4)
ll.display()

ll.replace_at_pos(3,1.2)
ll.replace_at_pos(4,1.4)
ll.display()

ll.remove_at_beginning()
ll.remove_at_beginning()
ll.display()

console.debug(ll.pop())
ll.display()



ll.insert_at_end(2)
ll.display()

console.debug(ll.get_elements_as_list())

console.debug(ll.remove_from_position(0))
ll.display()

console.debug(ll.remove_from_position(0))
console.debug(ll.remove_from_position(1))
ll.display()


console.debug(ll.pop())
ll.display()