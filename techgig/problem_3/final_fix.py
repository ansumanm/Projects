#!/usr/data/bin/python3

import sys
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import chain

efforts_list = []
D = 0
compute_once = False
min_effort = sys.maxsize

# Evaluate min effort
def effort_compute_fn(selector_tuple):
    # Initialize variables
    start = 0
    stop = 0
    sum_of_efforts = 0
    global D
    global efforts_list
    global compute_once
    global min_effort

    if all(elem == 1 for elem in selector_tuple):
        if compute_once is True:
            return sys.maxsize
        else:
            compute_once = True

    # Go through the effort list of doctors, select the 
    # efforts using the selector logic
    for i in range(0, D): 
        # print("@@@@@@@@@@@@@@@@@@@@@")
        # effort of doctor i
        effort = efforts_list[i]
        # print("effort: {} ".format(effort))

        # Number of efforts to select from this effort
        num_of_efforts = selector_tuple[i]
        # print("num_of_efforts %d" % num_of_efforts)


        # We are not selecting any effort from this doctor.
        if (num_of_efforts == 0):
            continue

        stop = start + num_of_efforts
        # print("start: {} stop: {}".format(start, stop))

        # Create a sublist out of effort
        sublist = effort[start:stop]
        # print("sublist: {}".format(sublist))

        sum_of_efforts += sum(sublist)
        # print("sum_of_efforts: {}".format(sum_of_efforts))

        # Speed it up further with early return
        if sum_of_efforts > min_effort:
            return sum_of_efforts 

        start = stop

    if min_effort < sum_of_efforts:
        min_effort = sum_of_efforts

    return sum_of_efforts


def main():
    global D
    global efforts_list
    global min_effort 

    P,D = input().split()

    # Get patients and doctors
    P = int(P)
    D = int(D)

    # Get effort list
    for e in range(0, D): 
        e_list = list(map(int, input().split()))
        efforts_list.append(e_list)

    # Calculate min effort.
    # Algo:
    # Divide number the patients to groups.
    # No. of groups = number of Doctors.
    # Group size constraint: 0 <= G <= P
    # For ex: 3 patients and 3 doctors
    # [0, 0, [0, 1, 2]]
    # [0, [0], [1, 2]]
    # [0, [0, 1], [2]]
    # [0, [0, 1, 2], 0]
    # [[0], [0], [1, 2]]
    # [[0], [1], [2]]
    # [[0], [1, 2], 0]
    # [[0, 1], [2], 0]
    # [[0, 1, 2], 0, 0]

    # effort_list_perm = list(permutations(efforts_list, D))

    # print(efforts_list)
    # print(effort_list_perm)

    # A doctor can select 0 to P doctors. Prepare that selector list
    selector_list = [*range(0, (P+1), 1)]

    # There are D doctors. Doctor D0 can select p1 patients, D1 can select
    # p2 patients. Prepare that combinbation iterable object.
    doctors_selection_comb = combinations_with_replacement(selector_list, D)

    """
    print(type(doctors_selection_comb))
    while True:
        try:
            print(next(doctors_selection_comb))
        except StopIteration:
            break
    """

    # Now filter the function
    # The above combination also contains selection where number of patients
    # are not equal to P. Remove all those combinations.
    doctors_filtered_combination = filter(lambda x: sum(x) == P, doctors_selection_comb)

    """
        print(type(doctors_filtered_combination))
        while True:
            try:
                print(next(doctors_filtered_combination))
            except StopIteration:
                break

        return
    """

    my_final_list = []

    # Now I need to permute the combination 
    # I have got (0, 4) (1, 3) (2, 2)
    # But I need (4, 0) (3, 1) also.

    # Make a list of permutations iters and chain them
    iters = []

    while True:
        try:
            tup = next(doctors_filtered_combination)

            """
            if all(elem == 1 for elem in tup):
                continue
            """

            iters.append(permutations(tup))
        except StopIteration:
            break

    # Add the skipped item once.
    # tuple_of_1s = tuple([1 for i in range(P)])
    # iters.append(iter(tuple_of_1s))


    # Finally chain them
    doctors_selector_chain = chain(*iters)

    """
    print(type(doctors_selector_chain))
    while True:
        try:
            print(next(doctors_selector_chain))
        except StopIteration:
            break

    return
    """


    for eff in map(effort_compute_fn, doctors_selector_chain):
        if eff < min_effort:
            min_effort = eff

    print(min_effort)

main()

