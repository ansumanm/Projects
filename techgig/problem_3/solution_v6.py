import sys
import itertools as it

def by_effort(elem):
    effort, ident = elem
    return effort

def main():
    efforts_list = []

    P,D = input().split()

    # Get patients and doctors
    P = int(P)
    D = int(D)

    # Get effort list
    for e in range(0, D): 
        e_list = list(map(int, input().split()))
        efforts_list.append(e_list)

    # For each patient, prepare a (effort, doctor_id) in sorted order
    # by effort
    patients_effort_data = []

    # Create empty lists
    for p in range(0, P):
        patients_effort_data.append([])

    for p in range(0, P):
        for d in range(0, D):
            patients_effort_data[p].append((efforts_list[d][p], d))

    for data in patients_effort_data:
        data.sort(key=by_effort)

    ident = 0
    for data in patients_effort_data:
        ident += 1

    iters = []
    for data in patients_effort_data:
        iters.append(iter(data))


    min_effort = sys.maxsize
    # This gets all paths.
    for tup in it.product(*iters):
        # The first occurence which satisfies 
        # the constraint is the solution.
        doctor_map = {}
        sum_of_efforts = 0
        previous_doctor_id = None
        path_rejected = False


        for p in range(0, P):
            effort, doctor_id = tup[p]
            sum_of_efforts += effort


            if doctor_id in doctor_map:
                # This doctor has already processed
                # We reject this path
                path_rejected = True
                break


            if previous_doctor_id is None:
                previous_doctor_id = doctor_id
                continue

            if previous_doctor_id == doctor_id:
                # This constraint is allowed
                continue

            # Set attendance of this doctor in map
            doctor_map[previous_doctor_id] = True
            previous_doctor_id = doctor_id


        if path_rejected is False:
            min_effort = sum_of_efforts
            break

    print(min_effort)



main()
