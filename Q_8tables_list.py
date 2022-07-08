import numpy as np
import pandas as pd
import random
import collections.abc

poss_scenarios = 'ABCD'
win_pattern = "ABCD"
iterations = 50
win_seq = win_pattern * iterations
games = len(win_seq)
base_reward = 10
act_step_cost = .5
int_step_allowance = 4
exp_rate = 0.2
alpha = 0.1  # learning rate
gamma = 0.8  # discount factor

if(input(" *****************Training settings*****************\n "
         "Win sequence: '{}'\n Iterations: {} \n Total games: {}\n Base reward: {}  Cost per step: {}\n "
         "Exploration rate: {}\n Learning rate: {}\n Type 'random' for random sequence instead, "
         "otherwise press enter to continue— ".format(win_pattern, iterations, games, base_reward,
                                                      act_step_cost, exp_rate, alpha))) == "random":
    rand_flag = True
    randletter = int(input(" What length of random repeating sequence? "))
    if 0 < randletter:
        win_pattern = random.choices(poss_scenarios, k=randletter)
        V = ''.join(win_pattern)
        iterations = int(input(" How many iterations? "))
        win_seq = V * iterations
        games = len(win_seq)
        input(
            " Randomly selected win pattern: {}\n Iterations: {}\n Total games: {}\n Press enter to continue—".format(
                V,
                iterations, games))
else:
    rand_flag = False

into_int_state = False
int_move_counter = int_step_allowance
act_move_counter = 1
game = 0
start_pos = (2, 2)
current_pos = start_pos
board_rows = 5
board_cols = 5
win_obj_A = (0, 0)
win_obj_B = (0, 4)
win_obj_C = (4, 0)
win_obj_D = (4, 4)
int_action_list = []
act_action_list = []
pos_act_rewards = {}
pos_int_rewards = {}
mini_dic = {}
board = {}
rewards_A = {}
rewards_B = {}
rewards_C = {}
rewards_D = {}
rewards_int_A = {}
rewards_int_B = {}
rewards_int_C = {}
rewards_int_D = {}
blank = {}
for i in range(board_rows):
    for j in range(board_cols):
        rewards_A[(i, j)] = 0
        rewards_B[(i, j)] = 0
        rewards_C[(i, j)] = 0
        rewards_D[(i, j)] = 0
        rewards_int_A[(i, j)] = 0
        rewards_int_B[(i, j)] = 0
        rewards_int_C[(i, j)] = 0
        rewards_int_D[(i, j)] = 0
        blank[(i, j)] = 0
for i in rewards_A:
    rewards_A[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                    (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
    rewards_B[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                    (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
    rewards_C[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                    (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
    rewards_D[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                    (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
    rewards_int_A[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                        (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
    rewards_int_B[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                        (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
    rewards_int_C[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                        (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
    rewards_int_D[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                        (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
    blank[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                        (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
act_actions = [
    "up",
    "down",
    "left",
    "right",
    "uleft",
    "uright",
    "dleft",
    "dright"]
int_actions = [
    "up",
    "down",
    "left",
    "right",
    "uleft",
    "uright",
    "dleft",
    "dright",
    "stay"]
act_action_trans = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (
    0, 1), "uleft": (-1, -1), "uright": (-1, 1), "dleft": (1, -1), "dright": (1, 1)}
int_action_trans = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (
    0, 1), "uleft": (-1, -1), "uright": (-1, 1), "dleft": (1, -1), "dright": (1, 1), "stay": (0, 0)}


def set_win_pos(letter):
    if letter == "A":
        winning_pos = win_obj_A
    elif letter == "B":
        winning_pos = win_obj_B
    elif letter == "C":
        winning_pos = win_obj_C
    else:
        winning_pos = win_obj_D
    return winning_pos


def take_next_move(action):
    if action == "up":
        next_pos = (current_pos[0] - 1, current_pos[1])
    elif action == "down":
        next_pos = (current_pos[0] + 1, current_pos[1])
    elif action == "left":
        next_pos = (current_pos[0], current_pos[1] - 1)
    elif action == "right":
        next_pos = (current_pos[0], current_pos[1] + 1)
    elif action == "stay":
        next_pos = (current_pos[0], current_pos[1])
    elif action == "uleft":
        next_pos = (current_pos[0] - 1, current_pos[1] - 1)
    elif action == "uright":
        next_pos = (current_pos[0] - 1, current_pos[1] + 1)
    elif action == "dleft":
        next_pos = (current_pos[0] + 1, current_pos[1] - 1)
    else:
        next_pos = (current_pos[0] + 1, current_pos[1] + 1)
    if (next_pos[0] >= 0) and (next_pos[0] <= (board_rows - 1)):
        if (next_pos[1] >= 0) and (next_pos[1] <= (board_cols - 1)):
            return next_pos
    return current_pos


def pick_act_move(win_target):
    while True:
        random.shuffle(act_actions)
        next_act_action = ""
        if np.random.uniform(0, 1) <= exp_rate:
            next_act_action = np.random.choice(act_actions)
        else:
            best_reward = -1000000
            for a in act_actions:
                if win_target == "A":
                    poss_reward = rewards_A[take_next_move(
                        a)][act_action_trans[a]]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
                elif win_target == "B":
                    poss_reward = rewards_B[take_next_move(
                        a)][act_action_trans[a]]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
                elif win_target == "C":
                    poss_reward = rewards_C[take_next_move(
                        a)][act_action_trans[a]]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
                else:
                    poss_reward = rewards_D[take_next_move(
                        a)][act_action_trans[a]]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
        new_position = take_next_move(next_act_action)
        if new_position == current_pos:
            continue
        else:
            return next_act_action


def pick_int_move(prev_target):
    while True:
        random.shuffle(act_actions)
        next_int_action = ""
        if np.random.uniform(0, 1) <= exp_rate:
            next_int_action = np.random.choice(int_actions)
        else:
            best_reward = -1000000
            for a in int_actions:
                if prev_target == "A":
                    poss_reward = rewards_int_A[take_next_move(
                        a)][int_action_trans[a]]
                    if poss_reward > best_reward:
                        next_int_action = a
                        best_reward = poss_reward
                elif prev_target == "B":
                    poss_reward = rewards_int_B[take_next_move(
                        a)][int_action_trans[a]]
                    if poss_reward > best_reward:
                        next_int_action = a
                        best_reward = poss_reward
                elif prev_target == "C":
                    poss_reward = rewards_int_C[take_next_move(
                        a)][int_action_trans[a]]
                    if poss_reward > best_reward:
                        next_int_action = a
                        best_reward = poss_reward
                else:
                    poss_reward = rewards_int_D[take_next_move(
                        a)][int_action_trans[a]]
                    if poss_reward > best_reward:
                        next_int_action = a
                        best_reward = poss_reward
        new_position = take_next_move(next_int_action)
        if new_position == current_pos and next_int_action != "stay":
            continue
        else:
            return next_int_action


def dict_update(d, update):
    for k, v in update.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = dict_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def update_act_rewards(reward_apply):
    reversed_act_list = unique(list(reversed(act_action_list)))
    for a, b in reversed_act_list:
        if scenario == "A":
            rewards_A[a][b] = round(
                rewards_A[a][b] + alpha * (reward_apply - rewards_A[a][b]), 2)
        elif scenario == "B":
            rewards_B[a][b] = round(
                rewards_B[a][b] + alpha * (reward_apply - rewards_B[a][b]), 2)
        elif scenario == "C":
            rewards_C[a][b] = round(
                rewards_C[a][b] + alpha * (reward_apply - rewards_C[a][b]), 2)
        else:
            rewards_D[a][b] = round(
                rewards_D[a][b] + alpha * (reward_apply - rewards_D[a][b]), 2)


def update_act_rewards_gamma(reward_apply):
    reversed_act_list = unique(list(reversed(act_action_list)))
    for a, b in reversed_act_list:
        if scenario == "A":
            rewards_A[a][b] = round(
                rewards_A[a][b] + alpha * (reward_apply + gamma *  - rewards_A[a][b]), 2)
        elif scenario == "B":
            rewards_B[a][b] = round(
                rewards_B[a][b] + alpha * (reward_apply - rewards_B[a][b]), 2)
        elif scenario == "C":
            rewards_C[a][b] = round(
                rewards_C[a][b] + alpha * (reward_apply - rewards_C[a][b]), 2)
        else:
            rewards_D[a][b] = round(
                rewards_D[a][b] + alpha * (reward_apply - rewards_D[a][b]), 2)


def update_int_rewards(reward_apply):
    if game == 0:
        return
    reversed_int_list = unique(list(reversed(int_action_list)))
    for a, b in reversed_int_list:
        if prev_scenario == "A":
            rewards_int_A[a][b] = round(
                rewards_int_A[a][b] + alpha * (reward_apply - rewards_int_A[a][b]), 2)
        elif prev_scenario == "B":
            rewards_int_B[a][b] = round(
                rewards_int_B[a][b] + alpha * (reward_apply - rewards_int_B[a][b]), 2)
        elif prev_scenario == "C":
            rewards_int_C[a][b] = round(
                rewards_int_C[a][b] + alpha * (reward_apply - rewards_int_C[a][b]), 2)
        else:
            rewards_int_D[a][b] = round(
                rewards_int_D[a][b] + alpha * (reward_apply - rewards_int_D[a][b]), 2)


def check_to_int():
    if int_move_counter < int_step_allowance and into_int_state:
        return True
    return False


def game_reset():
    global game, act_move_counter, temp_dict_act, temp_dict_int, pos_act_rewards, pos_int_rewards, into_int_state, int_action_list, act_action_list
    game += 1
    act_move_counter = 0
    int_action_list = []
    act_action_list = []
    into_int_state = True


def minisquare_values(reward_dic, board_pos):
    def show_board_squares():
        for i in range(board_rows):
            for j in range(board_cols):
                board[(i, j)] = "o"
        for a in board:
            if a == board_pos:
                board[a] = "XX"
        for i in range(0, board_rows):
            print(' --------------------------')
            out = ' | '
            for j in range(0, board_cols):
                out += str(board[(i, j)]).ljust(2) + ' | '
            print(out)
        print(' --------------------------')
    show_board_squares()
    if reward_dic == blank:
        z = "N/A"
    elif reward_dic == rewards_A:
        z = "AAA"
    elif reward_dic == rewards_B:
        z = "BBB"
    elif reward_dic == rewards_C:
        z = "CCC"
    elif reward_dic == rewards_D:
        z = "DDD"
    elif reward_dic == rewards_int_A:
        z = "I_A"
    elif reward_dic == rewards_int_B:
        z = "I_B"
    elif reward_dic == rewards_int_C:
        z = "I_C"
    else:
        z = "I_D"
    print(' {}------------- Pos{} -------------{}'.format(z, board_pos, z))
    for i in range(-1, 2):
        for j in range(-1, 2):
            mini_dic[(i, j)] = round((reward_dic[board_pos][(i, j)]), 1)
    for i in range(-1, 2):
        print(' -----------------------------------------')
        out = ' | '
        for j in range(-1, 2):
            out += str(float(mini_dic[(i, j)])).center(6) + '    |    '
        print(out)
    print(' {}------------- Pos{} -------------{}\n\n'.format(z, board_pos, z))
    return mini_dic


def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


while game < games:
    scenario = win_seq[game]
    # print("this is game number {} and the current scenario is {}".format(game, scenario))
    win_pos = set_win_pos(scenario)
    go_to_int = check_to_int()
    if go_to_int:
        int_action = pick_int_move(prev_scenario)
        int_action_coord = int_action_trans[int_action]
        int_action_list.append((current_pos, int_action_coord))
        current_pos = take_next_move(int_action)
        int_move_counter += 1
    else:
        into_int_state = False
        int_move_counter = 0
        if current_pos == win_pos:
            reward = base_reward - (act_move_counter * act_step_cost)
            update_act_rewards(reward)
            update_int_rewards(reward)
            if (game+1) % (games/10) == 0:
                print("Game {} of {} completed:  Act moves in last game: {}".format(
                    game + 1,
                    games,
                    act_move_counter))
            game_reset()
            prev_scenario = scenario
        else:  # take another move in action state
            act_action = pick_act_move(scenario)
            act_action_coord = act_action_trans[act_action]
            act_action_list.append((current_pos, act_action_coord))
            current_pos = take_next_move(act_action)
            act_move_counter += 1

if rand_flag:
    print(" Random sequence used: {}".format(V))
    print(" Iterations: {}".format(iterations))
else:
    print(" Sequence used: {}".format(win_pattern))
    print(" Iterations: {}".format(iterations))


# minisquare_values(rewards_A, (1, 3))
# minisquare_values(rewards_A, (1, 4))
# minisquare_values(rewards_A, (0, 3))
# minisquare_values(rewards_A, (0, 4))
#
# minisquare_values(rewards_A, (1, 3))
# minisquare_values(rewards_A, (1, 4))
# minisquare_values(rewards_A, (0, 3))
#
# minisquare_values(rewards_int_A, (0, 0))
# minisquare_values(rewards_int_A, (2, 2))
# minisquare_values(rewards_int_A, (0, 1))
# minisquare_values(rewards_int_A, (1, 0))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Data for visualizations
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
reward_dictionary_list = [rewards_A, rewards_B, rewards_C, rewards_D, rewards_int_A, rewards_int_B, rewards_int_C, rewards_int_D]
excel_name_list = ["rewards_A", "rewards_B", "rewards_C", "rewards_D", "rewards_int_A", "rewards_int_B", "rewards_int_C", "rewards_int_D"]
sheet_name_list = ["AA_", "BB", "CC", "DD," "intA_", "intB_", "intC_", "intD_"]


reward_info_out = {"scenA": [rewards_A, "rewards_A", "AA"], "scenB": [rewards_B, "rewards_B", "BB"], "scenC": [rewards_C, "rewards_C", "CC"]
                   , "scenD": [rewards_D, "rewards_D", "DD"], "intA": [rewards_int_A, "int_A", "intA"],
                   "intB": [rewards_int_B, "int_B", "intB"], "intC": [rewards_int_C, "int_C", "intC"],
                   "intD": [rewards_int_D, "int_D", "intD"]}

for a in reward_info_out:
    dic00 = minisquare_values(reward_info_out[a][0], (0, 0))
    v00_n1n1 = dic00[(-1, -1)]
    v00_n10 = dic00[(-1, 0)]
    v00_n11 = dic00[(-1, 1)]
    v00_0n1 = dic00[(0, -1)]
    v00_00 = dic00[(0, 0)]
    v00_01 = dic00[(0, 1)]
    v00_1n1 = dic00[(1, -1)]
    v00_10 = dic00[(1, 0)]
    v00_11 = dic00[(1, 1)]
    dic01 = minisquare_values(reward_info_out[a][0], (0, 1))
    v01_n1n1 = dic01[(-1, -1)]
    v01_n10 = dic01[(-1, 0)]
    v01_n11 = dic01[(-1, 1)]
    v01_0n1 = dic01[(0, -1)]
    v01_00 = dic01[(0, 0)]
    v01_01 = dic01[(0, 1)]
    v01_1n1 = dic01[(1, -1)]
    v01_10 = dic01[(1, 0)]
    v01_11 = dic01[(1, 1)]
    dic02 = minisquare_values(reward_info_out[a][0], (0, 2))
    v02_n1n1 = dic02[(-1, -1)]
    v02_n10 = dic02[(-1, 0)]
    v02_n11 = dic02[(-1, 1)]
    v02_0n1 = dic02[(0, -1)]
    v02_00 = dic02[(0, 0)]
    v02_01 = dic02[(0, 1)]
    v02_1n1 = dic02[(1, -1)]
    v02_10 = dic02[(1, 0)]
    v02_11 = dic02[(1, 1)]
    dic03 = minisquare_values(reward_info_out[a][0], (0, 3))
    v03_n1n1 = dic03[(-1, -1)]
    v03_n10 = dic03[(-1, 0)]
    v03_n11 = dic03[(-1, 1)]
    v03_0n1 = dic03[(0, -1)]
    v03_00 = dic03[(0, 0)]
    v03_01 = dic03[(0, 1)]
    v03_1n1 = dic03[(1, -1)]
    v03_10 = dic03[(1, 0)]
    v03_11 = dic03[(1, 1)]
    dic04 = minisquare_values(reward_info_out[a][0], (0, 4))
    v04_n1n1 = dic04[(-1, -1)]
    v04_n10 = dic04[(-1, 0)]
    v04_n11 = dic04[(-1, 1)]
    v04_0n1 = dic04[(0, -1)]
    v04_00 = dic04[(0, 0)]
    v04_01 = dic04[(0, 1)]
    v04_1n1 = dic04[(1, -1)]
    v04_10 = dic04[(1, 0)]
    v04_11 = dic04[(1, 1)]
    dic10 = minisquare_values(reward_info_out[a][0], (1, 0))
    v10_n1n1 = dic10[(-1, -1)]
    v10_n10 = dic10[(-1, 0)]
    v10_n11 = dic10[(-1, 1)]
    v10_0n1 = dic10[(0, -1)]
    v10_00 = dic10[(0, 0)]
    v10_01 = dic10[(0, 1)]
    v10_1n1 = dic10[(1, -1)]
    v10_10 = dic10[(1, 0)]
    v10_11 = dic10[(1, 1)]
    dic11 = minisquare_values(reward_info_out[a][0], (1, 1))
    v11_n1n1 = dic11[(-1, -1)]
    v11_n10 = dic11[(-1, 0)]
    v11_n11 = dic11[(-1, 1)]
    v11_0n1 = dic11[(0, -1)]
    v11_00 = dic11[(0, 0)]
    v11_01 = dic11[(0, 1)]
    v11_1n1 = dic11[(1, -1)]
    v11_10 = dic11[(1, 0)]
    v11_11 = dic11[(1, 1)]
    dic12 = minisquare_values(reward_info_out[a][0], (1, 2))
    v12_n1n1 = dic12[(-1, -1)]
    v12_n10 = dic12[(-1, 0)]
    v12_n11 = dic12[(-1, 1)]
    v12_0n1 = dic12[(0, -1)]
    v12_00 = dic12[(0, 0)]
    v12_01 = dic12[(0, 1)]
    v12_1n1 = dic12[(1, -1)]
    v12_10 = dic12[(1, 0)]
    v12_11 = dic12[(1, 1)]
    dic13 = minisquare_values(reward_info_out[a][0], (1, 3))
    v13_n1n1 = dic13[(-1, -1)]
    v13_n10 = dic13[(-1, 0)]
    v13_n11 = dic13[(-1, 1)]
    v13_0n1 = dic13[(0, -1)]
    v13_00 = dic13[(0, 0)]
    v13_01 = dic13[(0, 1)]
    v13_1n1 = dic13[(1, -1)]
    v13_10 = dic13[(1, 0)]
    v13_11 = dic13[(1, 1)]
    dic14 = minisquare_values(reward_info_out[a][0], (1, 4))
    v14_n1n1 = dic14[(-1, -1)]
    v14_n10 = dic14[(-1, 0)]
    v14_n11 = dic14[(-1, 1)]
    v14_0n1 = dic14[(0, -1)]
    v14_00 = dic14[(0, 0)]
    v14_01 = dic14[(0, 1)]
    v14_1n1 = dic14[(1, -1)]
    v14_10 = dic14[(1, 0)]
    v14_11 = dic14[(1, 1)]
    dic20 = minisquare_values(reward_info_out[a][0], (2, 0))
    v20_n1n1 = dic20[(-1, -1)]
    v20_n10 = dic20[(-1, 0)]
    v20_n11 = dic20[(-1, 1)]
    v20_0n1 = dic20[(0, -1)]
    v20_00 = dic20[(0, 0)]
    v20_01 = dic20[(0, 1)]
    v20_1n1 = dic20[(1, -1)]
    v20_10 = dic20[(1, 0)]
    v20_11 = dic20[(1, 1)]
    dic21 = minisquare_values(reward_info_out[a][0], (2, 1))
    v21_n1n1 = dic21[(-1, -1)]
    v21_n10 = dic21[(-1, 0)]
    v21_n11 = dic21[(-1, 1)]
    v21_0n1 = dic21[(0, -1)]
    v21_00 = dic21[(0, 0)]
    v21_01 = dic21[(0, 1)]
    v21_1n1 = dic21[(1, -1)]
    v21_10 = dic21[(1, 0)]
    v21_11 = dic21[(1, 1)]
    dic22 = minisquare_values(reward_info_out[a][0], (2, 2))
    v22_n1n1 = dic22[(-1, -1)]
    v22_n10 = dic22[(-1, 0)]
    v22_n11 = dic22[(-1, 1)]
    v22_0n1 = dic22[(0, -1)]
    v22_00 = dic22[(0, 0)]
    v22_01 = dic22[(0, 1)]
    v22_1n1 = dic22[(1, -1)]
    v22_10 = dic22[(1, 0)]
    v22_11 = dic22[(1, 1)]
    dic23 = minisquare_values(reward_info_out[a][0], (2, 3))
    v23_n1n1 = dic23[(-1, -1)]
    v23_n10 = dic23[(-1, 0)]
    v23_n11 = dic23[(-1, 1)]
    v23_0n1 = dic23[(0, -1)]
    v23_00 = dic23[(0, 0)]
    v23_01 = dic23[(0, 1)]
    v23_1n1 = dic23[(1, -1)]
    v23_10 = dic23[(1, 0)]
    v23_11 = dic23[(1, 1)]
    dic24 = minisquare_values(reward_info_out[a][0], (2, 4))
    v24_n1n1 = dic24[(-1, -1)]
    v24_n10 = dic24[(-1, 0)]
    v24_n11 = dic24[(-1, 1)]
    v24_0n1 = dic24[(0, -1)]
    v24_00 = dic24[(0, 0)]
    v24_01 = dic24[(0, 1)]
    v24_1n1 = dic24[(1, -1)]
    v24_10 = dic24[(1, 0)]
    v24_11 = dic24[(1, 1)]
    dic30 = minisquare_values(reward_info_out[a][0], (3, 0))
    v30_n1n1 = dic30[(-1, -1)]
    v30_n10 = dic30[(-1, 0)]
    v30_n11 = dic30[(-1, 1)]
    v30_0n1 = dic30[(0, -1)]
    v30_00 = dic30[(0, 0)]
    v30_01 = dic30[(0, 1)]
    v30_1n1 = dic30[(1, -1)]
    v30_10 = dic30[(1, 0)]
    v30_11 = dic30[(1, 1)]
    dic31 = minisquare_values(reward_info_out[a][0], (3, 1))
    v31_n1n1 = dic31[(-1, -1)]
    v31_n10 = dic31[(-1, 0)]
    v31_n11 = dic31[(-1, 1)]
    v31_0n1 = dic31[(0, -1)]
    v31_00 = dic31[(0, 0)]
    v31_01 = dic31[(0, 1)]
    v31_1n1 = dic31[(1, -1)]
    v31_10 = dic31[(1, 0)]
    v31_11 = dic31[(1, 1)]
    dic32 = minisquare_values(reward_info_out[a][0], (3, 2))
    v32_n1n1 = dic32[(-1, -1)]
    v32_n10 = dic32[(-1, 0)]
    v32_n11 = dic32[(-1, 1)]
    v32_0n1 = dic32[(0, -1)]
    v32_00 = dic32[(0, 0)]
    v32_01 = dic32[(0, 1)]
    v32_1n1 = dic32[(1, -1)]
    v32_10 = dic32[(1, 0)]
    v32_11 = dic32[(1, 1)]
    dic33 = minisquare_values(reward_info_out[a][0], (3, 3))
    v33_n1n1 = dic33[(-1, -1)]
    v33_n10 = dic33[(-1, 0)]
    v33_n11 = dic33[(-1, 1)]
    v33_0n1 = dic33[(0, -1)]
    v33_00 = dic33[(0, 0)]
    v33_01 = dic33[(0, 1)]
    v33_1n1 = dic33[(1, -1)]
    v33_10 = dic33[(1, 0)]
    v33_11 = dic33[(1, 1)]
    dic34 = minisquare_values(reward_info_out[a][0], (3, 4))
    v34_n1n1 = dic34[(-1, -1)]
    v34_n10 = dic34[(-1, 0)]
    v34_n11 = dic34[(-1, 1)]
    v34_0n1 = dic34[(0, -1)]
    v34_00 = dic34[(0, 0)]
    v34_01 = dic34[(0, 1)]
    v34_1n1 = dic34[(1, -1)]
    v34_10 = dic34[(1, 0)]
    v34_11 = dic34[(1, 1)]
    dic40 = minisquare_values(reward_info_out[a][0], (4, 0))
    v40_n1n1 = dic40[(-1, -1)]
    v40_n10 = dic40[(-1, 0)]
    v40_n11 = dic40[(-1, 1)]
    v40_0n1 = dic40[(0, -1)]
    v40_00 = dic40[(0, 0)]
    v40_01 = dic40[(0, 1)]
    v40_1n1 = dic40[(1, -1)]
    v40_10 = dic40[(1, 0)]
    v40_11 = dic40[(1, 1)]
    dic41 = minisquare_values(reward_info_out[a][0], (4, 1))
    v41_n1n1 = dic41[(-1, -1)]
    v41_n10 = dic41[(-1, 0)]
    v41_n11 = dic41[(-1, 1)]
    v41_0n1 = dic41[(0, -1)]
    v41_00 = dic41[(0, 0)]
    v41_01 = dic41[(0, 1)]
    v41_1n1 = dic41[(1, -1)]
    v41_10 = dic41[(1, 0)]
    v41_11 = dic41[(1, 1)]
    dic42 = minisquare_values(reward_info_out[a][0], (4, 2))
    v42_n1n1 = dic42[(-1, -1)]
    v42_n10 = dic42[(-1, 0)]
    v42_n11 = dic42[(-1, 1)]
    v42_0n1 = dic42[(0, -1)]
    v42_00 = dic42[(0, 0)]
    v42_01 = dic42[(0, 1)]
    v42_1n1 = dic42[(1, -1)]
    v42_10 = dic42[(1, 0)]
    v42_11 = dic42[(1, 1)]
    dic43 = minisquare_values(reward_info_out[a][0], (4, 3))
    v43_n1n1 = dic43[(-1, -1)]
    v43_n10 = dic43[(-1, 0)]
    v43_n11 = dic43[(-1, 1)]
    v43_0n1 = dic43[(0, -1)]
    v43_00 = dic43[(0, 0)]
    v43_01 = dic43[(0, 1)]
    v43_1n1 = dic43[(1, -1)]
    v43_10 = dic43[(1, 0)]
    v43_11 = dic43[(1, 1)]
    dic44 = minisquare_values(reward_info_out[a][0], (4, 4))
    v44_n1n1 = dic44[(-1, -1)]
    v44_n10 = dic44[(-1, 0)]
    v44_n11 = dic44[(-1, 1)]
    v44_0n1 = dic44[(0, -1)]
    v44_00 = dic44[(0, 0)]
    v44_01 = dic44[(0, 1)]
    v44_1n1 = dic44[(1, -1)]
    v44_10 = dic44[(1, 0)]
    v44_11 = dic44[(1, 1)]

    df00 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v00_n1n1, v00_n10, v00_n11, v00_0n1, v00_00, v00_01, v00_1n1, v00_10, v00_11]})
    df01 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v01_n1n1, v01_n10, v01_n11, v01_0n1, v01_00, v01_01, v01_1n1, v01_10, v01_11]})
    df02 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v02_n1n1, v02_n10, v02_n11, v02_0n1, v02_00, v02_01, v02_1n1, v02_10, v02_11]})
    df03 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v03_n1n1, v03_n10, v03_n11, v03_0n1, v03_00, v03_01, v03_1n1, v03_10, v03_11]})
    df04 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v04_n1n1, v04_n10, v04_n11, v04_0n1, v04_00, v04_01, v04_1n1, v04_10, v04_11]})
    df10 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v10_n1n1, v10_n10, v10_n11, v10_0n1, v10_00, v10_01, v10_1n1, v10_10, v10_11]})
    df11 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v11_n1n1, v11_n10, v11_n11, v11_0n1, v11_00, v11_01, v11_1n1, v11_10, v11_11]})
    df12 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v12_n1n1, v12_n10, v12_n11, v12_0n1, v12_00, v12_01, v12_1n1, v12_10, v12_11]})
    df13 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v13_n1n1, v13_n10, v13_n11, v13_0n1, v13_00, v13_01, v13_1n1, v13_10, v13_11]})
    df14 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v14_n1n1, v14_n10, v14_n11, v14_0n1, v14_00, v14_01, v14_1n1, v14_10, v14_11]})
    df20 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v20_n1n1, v20_n10, v20_n11, v20_0n1, v20_00, v20_01, v20_1n1, v20_10, v20_11]})
    df21 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v21_n1n1, v21_n10, v21_n11, v21_0n1, v21_00, v21_01, v21_1n1, v21_10, v21_11]})
    df22 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v22_n1n1, v22_n10, v22_n11, v22_0n1, v22_00, v22_01, v22_1n1, v22_10, v22_11]})
    df23 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v23_n1n1, v23_n10, v23_n11, v23_0n1, v23_00, v23_01, v23_1n1, v23_10, v23_11]})
    df24 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v24_n1n1, v24_n10, v24_n11, v24_0n1, v24_00, v24_01, v24_1n1, v24_10, v24_11]})
    df30 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v30_n1n1, v30_n10, v30_n11, v30_0n1, v30_00, v30_01, v30_1n1, v30_10, v30_11]})
    df31 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v31_n1n1, v31_n10, v31_n11, v31_0n1, v31_00, v31_01, v31_1n1, v31_10, v31_11]})
    df32 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v32_n1n1, v32_n10, v32_n11, v32_0n1, v32_00, v32_01, v32_1n1, v32_10, v32_11]})
    df33 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v33_n1n1, v33_n10, v33_n11, v33_0n1, v33_00, v33_01, v33_1n1, v33_10, v33_11]})
    df34 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v34_n1n1, v34_n10, v34_n11, v34_0n1, v34_00, v34_01, v34_1n1, v34_10, v34_11]})
    df40 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v40_n1n1, v40_n10, v40_n11, v40_0n1, v40_00, v40_01, v40_1n1, v40_10, v40_11]})
    df41 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v41_n1n1, v41_n10, v41_n11, v41_0n1, v41_00, v41_01, v41_1n1, v41_10, v41_11]})
    df42 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v42_n1n1, v42_n10, v42_n11, v42_0n1, v42_00, v42_01, v42_1n1, v42_10, v42_11]})
    df43 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v43_n1n1, v43_n10, v43_n11, v43_0n1, v43_00, v43_01, v43_1n1, v43_10, v43_11]})
    df44 = pd.DataFrame({'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1], 'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:','value:','value:','value:'], 'value': [v44_n1n1, v44_n10, v44_n11, v44_0n1, v44_00, v44_01, v44_1n1, v44_10, v44_11]})

    pivot00 = df00.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot01 = df01.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot02 = df02.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot03 = df03.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot04 = df04.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot10 = df10.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot11 = df11.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot12 = df12.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot13 = df13.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot14 = df14.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot20 = df20.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot21 = df21.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot22 = df22.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot23 = df23.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot24 = df24.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot30 = df30.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot31 = df31.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot32 = df32.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot33 = df33.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot34 = df34.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot40 = df40.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot41 = df41.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot42 = df42.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot43 = df43.pivot(index='X-direction', columns='Y-direction', values='value')
    pivot44 = df44.pivot(index='X-direction', columns='Y-direction', values='value')

    writer = pd.ExcelWriter(reward_info_out[a][1] + '.xlsx', engine='xlsxwriter')
    pivot00.to_excel(writer, sheet_name=reward_info_out[a][2] + '00')
    pivot01.to_excel(writer, sheet_name=reward_info_out[a][2] + '01')
    pivot02.to_excel(writer, sheet_name=reward_info_out[a][2] + '02')
    pivot03.to_excel(writer, sheet_name=reward_info_out[a][2] + '03')
    pivot04.to_excel(writer, sheet_name=reward_info_out[a][2] + '04')
    pivot10.to_excel(writer, sheet_name=reward_info_out[a][2] + '10')
    pivot11.to_excel(writer, sheet_name=reward_info_out[a][2] + '11')
    pivot12.to_excel(writer, sheet_name=reward_info_out[a][2] + '12')
    pivot13.to_excel(writer, sheet_name=reward_info_out[a][2] + '13')
    pivot14.to_excel(writer, sheet_name=reward_info_out[a][2] + '14')
    pivot20.to_excel(writer, sheet_name=reward_info_out[a][2] + '20')
    pivot21.to_excel(writer, sheet_name=reward_info_out[a][2] + '21')
    pivot22.to_excel(writer, sheet_name=reward_info_out[a][2] + '22')
    pivot23.to_excel(writer, sheet_name=reward_info_out[a][2] + '23')
    pivot24.to_excel(writer, sheet_name=reward_info_out[a][2] + '24')
    pivot30.to_excel(writer, sheet_name=reward_info_out[a][2] + '30')
    pivot31.to_excel(writer, sheet_name=reward_info_out[a][2] + '31')
    pivot32.to_excel(writer, sheet_name=reward_info_out[a][2] + '32')
    pivot33.to_excel(writer, sheet_name=reward_info_out[a][2] + '33')
    pivot34.to_excel(writer, sheet_name=reward_info_out[a][2] + '34')
    pivot40.to_excel(writer, sheet_name=reward_info_out[a][2] + '40')
    pivot41.to_excel(writer, sheet_name=reward_info_out[a][2] + '41')
    pivot42.to_excel(writer, sheet_name=reward_info_out[a][2] + '42')
    pivot43.to_excel(writer, sheet_name=reward_info_out[a][2] + '43')
    pivot44.to_excel(writer, sheet_name=reward_info_out[a][2] + '44')
    writer.save()
