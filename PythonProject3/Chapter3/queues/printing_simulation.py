"""
Consider the following situation in a computer science laboratory. On any average day about 10 students are working in
the lab at any given hour. These students typically print up to twice during that time, and the length of these tasks
 ranges from 1 to 20 pages. The printer in the lab is older, capable of processing 10 pages per minute of draft quality.
  The printer could be switched to give better quality, but then it would produce only five pages per minute.
  The slower printing speed could make students wait too long. What page rate should be used?
We could decide by building a simulation that models the laboratory. We will need to construct representations for
students, printing tasks, and the printer (Figure 4). As students submit printing tasks, we will add them to a waiting
list, a queue of print tasks attached to the printer. When the printer completes a task, it will look at the queue to
see if there are any remaining tasks to process. Of interest for us is the average amount of time students will wait
for their papers to be printed. This is equal to the average amount of time a task waits in the queue.
To model this situation we need to use some probabilities. For example, students may print a paper from 1 to 20 pages
in length. If each length from 1 to 20 is equally likely, the actual length for a print task can be simulated by using
a random number between 1 and 20 inclusive. This means that there is equal chance of any length from 1 to 20 appearing.
If there are 10 students in the lab and each prints twice, then there are 20 print tasks per hour on average. What is
the chance that at any given second, a print task is going to be created? The way to answer this is to consider the
ratio of tasks to time. Twenty tasks per hour means that on average there will be one task every 180 seconds:
For every second we can simulate the chance that a print task occurs by generating a random number between 1 and 180
inclusive. If the number is 180, we say a task has been created. Note that it is possible that many tasks could be
created in a row or we may wait quite a while for a task to appear. That is the nature of simulation. You want to
simulate the real situation as closely as possible given that you know general parameters.

MAIN SIMULATION STEPS
1. Create a queue of printing tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.
2. For each second (current_second):
    - does a new print task get created? If so, add it to the queue with the current_second as the timestamp.
    - if the printer is not busy and if a task is waiting,
        - remove the next task from the print queue and assign it to the printer.
        - subtract the timestamp from the current_second to compute the waiting time for that task.
        - append the waiting time for that task to a list for later processing
        - based on the number of pages in the print task, figure out how much time will be required
    - The printer now does one second of printing if necessary. It also subtracts one second from the time required for that task
    - if the task has been completed, in other words the time required has reached zero, the printer is no longer busy
3. After the simulation is complete, compute the average waiting time from the list of waiting times generated

To design this simulation we will create classes for the three real-world objects described above: Printer, Task, and PrintQueue
The Printer class will need to track whether it has a current task. If it does, then it is busy and the amount of time
needed can be computed from the number of pages in the task. The constructor will also allow the pages-per-minute setting
to be initialized. The tick method decrements the internal timer and sets the printer to idle if the task is completed
"""
class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

"""
The Task class will represent a single printing task. When the task is created, a random generator will provide 
a length from 1 to 20 pages. We have chosen to use the randrange function from the random module
"""
import random
class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp

"""
The main simulation implements the algorithm described above. The print_queue object is an instance of our existing queue ADT.
A boolean helper function, new_print_task, decides whether a new printing task has been created. We have again chosen to
use the randrange function from the random module to return a random integer between 1 and 180. Print tasks arrive once 
every 180 seconds. By arbitrarily choosing 180 from the range of random integers, we can simulate this random event. 
The simulation function allows us to set the total time and the pages per minute for the printer.
"""

import queues
def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = queues.Queue()
    waiting_time = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            nexttask = print_queue.dequeue()
            waiting_time.append(nexttask.wait_time(current_second))
            lab_printer.start_next(nexttask)
        lab_printer.tick()

    average_wait = sum(waiting_time) / len(waiting_time)
    print(
        f"Average Wait {average_wait:6.2f} secs" + f"{print_queue.size():3d} task remaining."
    )

def new_print_task():
    num = random.randrange(1, 181)
    return num == 180

for i in range(10):
    simulation(3600, 5)
