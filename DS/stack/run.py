import sys,os
dir_path = os.path.dirname((os.path.dirname(os.path.realpath(__file__))))
sys.path.append(dir_path)

from stack.impl import StackImpl
from my_package.console import _console as console


test=StackImpl(10)

for i in range(4):
    try:
        test.push(i*10)
    except Exception as e:
        console.error(e)

test.display()

print(test.pop(2))


test.display()


for i in range(6):
    try:
        console.info("pop "+str(test.pop()))
    except Exception as e:
        console.error(e)

for i in range(15):
    try:
        test.push(i*10)
    except Exception as e:
        console.error(e)

console.debug(test.get_values())


console.info(test)
