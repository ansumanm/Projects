#!/usr/data/bin/python3
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def main():
    efforts_list = []
    min_effort = sys.maxsize

    P,D = input().split()

    # Get patients and doctors
    P = int(P)
    D = int(D)

    # Get effort list
    for e in range(0, D): 
        e_list = list(map(int, input().split()))
        efforts_list.append(e_list)

        total_effort = sum(e_list)

        if total_effort < min_effort:
            min_effort = total_effort

    print("Benchmark effort: %d" % min_effort)

    # Compute and effort_list for patients
    efforts_list_patients = []

    for p in range(0, P):
        efforts_p = []
        for d in range(0, D):
            efforts_p.append(efforts_list[d][p])

        efforts_list_patients.append(efforts_p)

    root_list = []
    # For backtracking, we use depth
    for p in range(0, P):


    return
        

    # In this logic, we just choose the doctor with the least 
    # effort for that patient. If 2 doctors have same effort
    # for a patient, then we need to evaluate both the options.
    # Once a doctor has been processed, it has to be removed from 
    # the choice.

    # Compute and effort_list for patients
    efforts_list_patients = []

    for p in range(0, P):
        efforts_p = []
        for d in range(0, D):
            efforts_p.append(efforts_list[d][p])

        efforts_list_patients.append(efforts_p)

    # A solution using backtracking


main()
