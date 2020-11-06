
# Press Shift+F10 to execute script
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
if __name__ == '__main__':                  #module looks at it's own name value to see if
                                            #it is being run directly or called into another program
    print('This module is being run directly (not imported from another module)')
else:
    print('This module has been imported into another module to run')

lengthstring = len("Hello")
print("the variable 'lengthstring' is of type", type(lengthstring))        # will print out what type of variable 'lengthstring' is

def print_hi(name):
    # Use a breakpoint (red dot) in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

name = 'Rachel'
print_hi(name)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


runners = { 1000: 'Jack', 1001: 'Eric', 1002: 'Lisa' }            #the keys here are 1000, 1001, etc
print(runners[1001])
runners[1003] = 'Sara'                               # adding an entry pair to the dictionary
for r in runners:
    print("runner no {} : {}".format(r, runners[r]))
for r, name in runners.items():
    print("no: {} = {}".format(r, name))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

list1 = ['bob', 'jack and jenny', '342 567', '457yut']
print(list1[0])
new_item = enumerate(list1)
print(type(new_item))
print(enumerate(list1))
for i, item in enumerate(list1):
    print(i,item)
