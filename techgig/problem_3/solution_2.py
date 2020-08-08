#!/usr/data/bin/python3
import sys

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


    last_doctor_used = None
    min_effort = 0
    for p in range(0, P):
        print(efforts_list_patients)
        least_effort = min(efforts_list_patients[p])

        doctor_used = efforts_list_patients[p].index(least_effort)

        print("doctor_used: %d " % doctor_used)
        if last_doctor_used is not None:
            print("last_doctor_used : %d " % last_doctor_used)
            if doctor_used != last_doctor_used:
                # Make sure that the doctor's choices are struck off
                # for further choices
                for x in range((p+1), P):
                    efforts_list_patients[x][last_doctor_used] = sys.maxsize

        last_doctor_used = doctor_used

        min_effort += least_effort

    print(min_effort)
    

main()
