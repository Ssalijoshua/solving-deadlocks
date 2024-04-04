# Such that we dont have to loop through the lists to find the sum and totals
import numpy as np

# DETECTION ALGORITHMS IMPLEMENTATION

# User inputs
available_resources = np.array(list(map(int,input("Enter the resources that are currently available and seperate with commas").split(","))))

num_processes =  int(input("How many processes are you going to work with?"))
    
allocation = []
request = []


for i in range(num_processes):
    x = np.array(list(map(int,input("Enter the allocation matrix seperating with commas").split(","))))
    allocation.append(x)

    y = np.array(list(map(int,input("Enter the requested values seperating with commas ").split(","))))
    request.append(y)

retry = 10

# List to store the execution status of each process either True or False
status = [False] * num_processes

# List to store all executed process_ids
executed = []


class detect_deadlock:
    def __init__(self, allocation,request,available):
        self.allocation = allocation
        self.request = request
        self.available = available
        self.num_processes = num_processes
        # Number of times we can retry after some_processes have failed to execute
        self.retry = retry

    def check_deadlock(self):
        
        # creating a variable to access indexes of list status 
        for process_id in range(self.num_processes):
                
                if status[process_id] == False:
                            if all(self.request[process_id] <= self.available):
                                status[process_id] = True
                                self.available += self.allocation[process_id]

                                # so that when we iterate, the executed process cant be executed again
                                self.allocation[process_id] -= self.allocation[process_id]
                                executed.append(process_id)
                                
        if all(status) or self.retry==0:
            if self.retry ==0:
                 print("Deadlock occured")
            return f"The execution sequence is {executed}"
        else:
            print("_________________________________________")
            print(f"Some processes didnt execute __RETRYING__ {self.retry} times")                
            self.retry-=1
            self.check_deadlock()
                
            return f"Executed processses:{executed}"


# allocation = [
#     np.array([0, 1, 0]),
#     np.array([2, 0, 0]),
#     np.array([3, 0, 3]),
#     np.array([2, 1, 1]),
#     np.array([0, 0, 2])
# ]

# request = [
#     np.array([0, 0, 0]),
#     np.array([2, 0, 2]),
#     np.array([0, 0, 0]),
#     np.array([1, 0, 0]),
#     np.array([0, 0, 2])
# ]

# available_resources = [0, 0, 0]

detector = detect_deadlock(allocation, request, available_resources)
x= detector.check_deadlock()

print(x)