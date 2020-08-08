import sys
import itertools as it

def main():
    P,D = input().split()
    efforts_list = []

    # Get patients and doctors
    P = int(P)
    D = int(D)

    # Get effort list
    for e in range(0, D): 
        e_list = list(map(int, input().split()))
        efforts_list.append(e_list)

    min_effort = sum(efforts_list[0])
    print("Min effort: %d" % min_effort)
    """
    Constraints:
    1<= D <=10
    0<= Efforts <=1000
    1<= P <=20
    """
    max_D = 10
    max_P = 20

    max_P = 6
    max_D = 3

    max_efforts_list = []

    for d in range(0, max_D):
        d_effort = []
        for p in range(0, max_P):
            if p < P and d < D:
                d_effort.append(efforts_list[d][p])
            else:
                if d < D:
                    d_effort.append(0)
                else:
                    d_effort.append(sys.maxsize)

        max_efforts_list.append(d_effort)

    print(max_efforts_list)

    # My 10x20 matrix is created. 
    # Create a tree of iterators, where we terminate the 
    # iteration when effort becomes greater than min_effort
    max_P = 6
    max_D = 3

    selector_list = [*range(0, (max_P+1), 1)]
    doctors_selection_comb = it.combinations_with_replacement(selector_list, max_D)


    doctors_filtered_combination = filter(lambda x: sum(x) == max_P, doctors_selection_comb)

    for tup in doctors_filtered_combination:
        print(tup)

    return

    iters = []
    for tup in doctors_filtered_combination:
        iters.append(it.permutations(tup))

    print(len(iters))

    for ite in iters:
        print("********")
        for tup in ite:
            print(tup)



main()
