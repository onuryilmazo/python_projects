from collections import deque
'''
deque(["a", "b", "c"])
deque(["abc"])
deque([{"data":"a"},{"data":"b"}])

llist = deque("abcde")
print(llist)
llist.append("f")
print(llist)
llist.pop()
print(llist)
llist.appendleft("z")
print(llist)
llist.popleft()
print(llist)
'''

'''
QUEUES
FIFO 
'''

queue = deque()
queue.append("Mary")
queue.append("John")
queue.append("Susan")
print(queue)
'''
This example stands for restaurant seating guests. 
If it is fully booked we should lift the sitting guests starting from first come
'''
queue.popleft()
print(queue)
queue.append("new customer")
print(queue)

'''
STACKS
LIFO approach 
Imagine you’re creating a web browser’s history functionality in which store every page a user visits so they can go back in time easily. 
Assume these are the actions a random user takes on their browse
'''
history = deque()

history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")
print(history)
history.popleft()
print(history)
