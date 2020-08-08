#!/usr/data/bin/python3
def evaluate_max_wins(testcase):
    n_members = testcase['n_members']
    g_powers = testcase['g_powers']
    o_powers = testcase['o_powers']

    wins = 0

    g_powers.sort(reverse=True)
    o_powers.sort(reverse=True)
    print(g_powers)
    print(o_powers)

    for x in range(0, n_members):
        if o_powers[x] >= g_powers[x]:
            # remove the last element of g_powers
            last_ele = g_powers[n_members - 1]
            g_powers.pop(n_members - 1)
            g_powers.insert(x, last_ele)
        else:
            wins+=1

        
    print("Optimum solution:")
    print(g_powers)
    print(o_powers)
    return wins

def main():
    testcases = []
    n_testcases = int(input())

    for t in range(0, n_testcases):
        n_members = int(input())
        G_powers = input().split()
        opponent_powers = input().split()

        testcase = {}
        testcase['n_members'] = int(n_members)
        testcase['g_powers'] = list(map(int, G_powers))
        testcase['o_powers'] = list(map(int, opponent_powers))

        testcases.append(testcase)

    print(testcases)

    max_wins = 0
    for testcase in testcases:
        max_wins = evaluate_max_wins(testcase)
        print(max_wins)

main()

