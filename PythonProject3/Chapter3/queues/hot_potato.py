"""
We will implement a general simulation of Hot Potato. Our program will input a list of names and a constant, call it “num,”
to be used for counting. It will return the name of the last person remaining after repetitive counting by num.
What happens at that point is up to you.

To simulate the circle, we will use a queue (see Figure 3). Assume that the child holding the potato will be at the
front of the queue. Upon passing the potato, the simulation will simply dequeue and then immediately enqueue that child,
 putting them at the end of the line. They will then wait until all the others have been at the front before it will be
 their turn again. After num dequeue/enqueue operations, the child at the front will be removed permanently and another
 cycle will begin. This process will continue until only one name remains (the size of the queue is 1).
"""

import queues

def hot_potato(names, num):
    name_queue = queues.Queue()
    for name in names:
        name_queue.enqueue(name)

    while name_queue.size() > 1:
        for i in range(num):
            front = name_queue.dequeue()
            name_queue.enqueue(front)
        name_queue.dequeue()

    return name_queue.dequeue()

if __name__ == '__main__':
    name_list = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    print(hot_potato(name_list, 7))