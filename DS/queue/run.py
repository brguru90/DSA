import sys,os
dir_path = os.path.dirname(os.path.dirname((os.path.dirname(os.path.realpath(__file__)))))
sys.path.append(dir_path)

from DS.queue.impl import QueueImpl
from DS.my_package.console import _console as console




test=QueueImpl(10)
console.info(test)

for i in range(4):
    try:
        test.insert(i*10)
    except Exception as e:
        console.error(e)

test.display()
print(test.remove(2))
test.display()

for i in range(6):
    try:
        console.info("remove "+str(test.remove()))
    except Exception as e:
        console.error(str(e)+","+str(i))


for i in range(15):
    try:
        test.insert(i*10)
    except Exception as e:
        console.error(str(e)+","+str(i))

console.debug(test.get_values())


console.info(test)

test.free()

console.info(test)


