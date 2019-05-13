"""
Win or lose
"""

def check_win_or_lose(number_of_players, villian_strength, player_energy):
    villian_strength_list = villian_strength.split(" ")
    player_energy_list = player_energy.split(" ")

    villian_strength_list = list(map(int, villian_strength_list))
    player_energy_list = list(map(int, player_energy_list))

    villian_strength_list.sort(reverse=True)
    player_energy_list.sort(reverse=True)

    if villian_strength_list < player_energy_list:
        return "WIN"
    else:
        return "LOSE"




def main():
    num_testcases = input()
    for x in range(int(num_testcases)):
        number_of_players = input()
        villian_strength = input()
        player_energy = input()
        result = check_win_or_lose(number_of_players, villian_strength, player_energy)
        print(result)

main()
