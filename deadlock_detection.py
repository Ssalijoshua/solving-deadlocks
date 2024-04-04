# Using numpy arrays such that I can subtract the lists directly without having to point out elements

import numpy as np

# Looks like I will have to implement the detection algorithm in python
# Specfying the total size of the resources
# For the start I am working with A B and C
# To enter the total resources for the system
Total_r = input("Enter the total resources for A, B and C on the respective order").split(",")
Total_r = [int(x) for x in Total_r]
Total_r = np.array(Total_r)
print(Total_r)

# Entering the allocation and request for p1(process 1)
p1_allocation= input("Enter the allocated resources for process 1 in their respective order").split(",")
    # Just converting them the values to integers
p1_allocation = [int(x) for x in p1_allocation]
p1_allocation = np.array(p1_allocation)
print(p1_allocation)

p1_request= input("Enter the  resources requested for by process 1 in their respective order").split(",")
p1_request = [int(x) for x in p1_request]
p1_request = np.array(p1_request)
print(p1_request)

# Entering the allocation and request for p2(process 2)
p2_allocation= input("Enter the allocated resources for process 2 in their respective order").split(",")
    # Just converting them the values to integers
p2_allocation = [int(x) for x in p2_allocation]
p2_allocation = np.array(p2_allocation)
print(p2_allocation)

p2_request= input("Enter the  resources requested for by process 2 in their respective order").split(",")
p2_request = [int(x) for x in p2_request]
p2_request = np.array(p2_request)
print(p2_request)


# Entering the allocation and request for p3(process 3)
p3_allocation= input("Enter the allocated resources for process 3 in their respective order").split(",")
    # Just converting them the values to integers
p3_allocation = [int(x) for x in p3_allocation]
p3_allocation = np.array(p3_allocation)
print(p3_allocation)

p3_request= input("Enter the  resources requested for by process 3 in their respective order").split(",")
p3_request = [int(x) for x in p3_request]
p3_request = np.array(p3_request)
print(p3_request)

# Entering the allocation and request for p4(process 4)
p4_allocation= input("Enter the allocated resources for process 4 in their respective order").split(",")
    # Just converting them the values to integers
p4_allocation = [int(x) for x in p4_allocation]
p4_allocation = np.array(p4_allocation)
print(p4_allocation)

p4_request= input("Enter the  resources requested for by process 4 in their respective order").split(",")
p4_request = [int(x) for x in p4_request]
p4_request = np.array(p4_request)
print(p4_request)

# Entering the allocation and request for p5(process 5)
p5_allocation= input("Enter the allocated resources for process 5 in their respective order").split(",")
    # Just converting them the values to integers
p5_allocation = [int(x) for x in p5_allocation]
p5_allocation = np.array(p5_allocation)
print(p5_allocation)

p5_request= input("Enter the  resources requested for by process 5 in their respective order").split(",")
p5_request = [int(x) for x in p5_request]
p5_request = np.array(p5_request)
print(p5_request)



#function for getting the safe sequence
def get_sequence():
    safe_sequence=[]

    # Originally the available is the Total resources - allocated
    available = Total_r - (p1_allocation + p2_allocation + p3_allocation + p4_allocation + p5_allocation)
    print(available)  

    # Initializing the dictionary for to store values processess  
    execution_status = {"p1":False,"p2":False,"p3":False,"p4":False,"p5":False}

    if p1_request[0] <= available[0] and p1_request[1] <= available[1] and p1_request[2] <= available[2]:
        execution_status["p1"] = True
        # releasing allocated resources
        available += p1_allocation
        safe_sequence.append('p1')
    
    else:
        print("Process 1 pending execution")


    if p2_request[0] <= available[0] and p2_request[1] <= available[1] and p2_request[2] <= available[2]:
        execution_status["p2"] = True
        # releasing allocated resources
        available += p2_allocation
        safe_sequence.append('p2')
    
    else:
        print("Process 2 pending execution")


    if p3_request[0] <= available[0] and p3_request[1] <= available[1] and p3_request[2] <= available[2]:
        execution_status["p3"] = True
        # releasing allocated resources
        available += p3_allocation
        safe_sequence.append('p3')
    
    else:
        print("Process 3 pending execution")

    
    if p4_request[0] <= available[0] and p4_request[1] <= available[1] and p4_request[2] <= available[2]:
        execution_status["p4"] = True
        # releasing allocated resources
        available += p4_allocation
        safe_sequence.append('p4')
    
    else:
        print("Process 4 pending execution")


    if p5_request[0] <= available[0] and p5_request[1] <= available[1] and p5_request[2] <= available[2]:
        execution_status["p5"] = True
        # releasing allocated resources
        available += p5_allocation
        safe_sequence.append('p5')
    
    else:
        print("Process 5 pending execution")


    return safe_sequence

print(get_sequence())