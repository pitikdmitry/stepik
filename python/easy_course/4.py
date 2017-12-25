n = int(input())
teams = {}


def team_exists(goals_1: int, team_1: str, goals_2: int, teams: {}) -> None:
    team_1_stats = teams.get(team_1)
    team_1_stats[0] = team_1_stats[0] + 1# all games
    sum_points = 0

    # wins
    if goals_1 > goals_2:
        team_1_stats[1] = team_1_stats[1] + 1
        sum_points += 3

    # ni4
    if goals_1 == goals_2:
        team_1_stats[2] = team_1_stats[2] + 1
        sum_points += 1

    # looses
    if goals_1 < goals_2:
        team_1_stats[3] = team_1_stats[3] + 1

    team_1_stats[4] = team_1_stats[4] + sum_points
    teams[team_1] = team_1_stats


def team_not_exists(goals_1: int, team_1: str, goals_2: int, teams: {}) -> None:
    team_1_stats = []
    team_1_stats.append(1)  # all games
    sum_points = 0

    # wins
    if goals_1 > goals_2:
        team_1_stats.append(1)
        sum_points += 3
    elif goals_1 <= goals_2:
        team_1_stats.append(0)

    # ni4
    if goals_1 == goals_2:
        sum_points += 1
        team_1_stats.append(1)
    else:
        team_1_stats.append(0)

    # looses
    if goals_1 < goals_2:
        team_1_stats.append(1)
    elif goals_1 >= goals_2:
        team_1_stats.append(0)

    team_1_stats.append(sum_points)
    teams[team_1] = team_1_stats


def process(goals_1: int, team_1: str, goals_2: int, team_2: str, teams: {}) -> None:
    if team_1 in teams:
        team_exists(goals_1, team_1, goals_2, teams)
    else:
        team_not_exists(goals_1, team_1, goals_2, teams)

    if team_2 in teams:
        team_exists(goals_2, team_2, goals_1, teams)
    else:
        team_not_exists(goals_2, team_2, goals_1, teams)

    return


def process_input() -> None:
    input_list = []
    input_list = input().split(";")
    process(int(input_list[1]), input_list[0], int(input_list[3]), input_list[2], teams)


for i in range(0, n):
    process_input()
# 3 Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2


for key, value in teams.items():
    print(key + ":" + str(value[0]) + " " + str(value[1]) + " " + str(value[2]) + " " + str(value[3]) + " " + str(value[4]))
