"""
Notes:

"""
import numpy as np
import random
import collections.abc
import seaborn as sb
import matplotlib.pyplot as plt

# input desired paramters
poss_scenarios = 'ABCD'
win_pattern = "A"
iterations = 10000
win_seq = win_pattern * iterations
games = len(win_seq)
base_reward = 10
act_step_cost = 0
int_step_allowance = 4
exp_rate = 0.2
learn_rate = 0.5

if(input(" *****************Training settings*****************\n "
         "Win sequence: '{}'\n Iterations: {} \n Total games: {}\n Base reward: {}  Cost per step: {}\n "
         "Exploration rate: {}\n Learning rate: {}\n Type 'random' for random sequence instead, "
         "otherwise press enter to continue— ".format(win_pattern, iterations, games, base_reward,
          act_step_cost, exp_rate, learn_rate))) == "random":
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

# initialize starting variables
into_int_state = False
int_move_counter = int_step_allowance
act_move_counter = 1
game = 0
start_pos = (2, 2)
current_pos = start_pos
pos_act_rewards = {}
pos_int_rewards = {}
mini_dic = {}
board = {}

# allowed actions by state
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


# board initialization and rules
board_rows = 5
board_cols = 5

# set locations of win scenarios and initialize separate reward tables to 0
win_obj_A = (0, 0)
win_obj_B = (0, 4)
win_obj_C = (4, 0)
win_obj_D = (4, 4)
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


def update_act_rewards(rwd_actpos_dic, reward_apply):
    if scenario == "A":
        for a in rwd_actpos_dic:
            for b in rwd_actpos_dic[a]:
                rewards_A[a][b] = round(
                    (1-learn_rate) * rewards_A[a][b] + learn_rate * (reward_apply - rewards_A[a][b]), 2)
    elif scenario == "B":
        for a in rwd_actpos_dic:
            for b in rwd_actpos_dic[a]:
                rewards_B[a][b] = round(
                    rewards_B[a][b] + learn_rate * (reward_apply - rewards_B[a][b]), 2)
    elif scenario == "C":
        for a in rwd_actpos_dic:
            for b in rwd_actpos_dic[a]:
                rewards_C[a][b] = round(
                    rewards_C[a][b] + learn_rate * (reward_apply - rewards_C[a][b]), 2)
    else:
        for a in rwd_actpos_dic:
            for b in rwd_actpos_dic[a]:
                rewards_D[a][b] = round(
                    rewards_D[a][b] + learn_rate * (reward_apply - rewards_D[a][b]), 2)


def update_int_rewards(rwd_intpos_dic, reward_apply):
    if game == 0:
        return
    elif prev_scenario == "A":
        # print("the game is {} and the previous scenario to be rewarded is {} before resetting".format(game, prev_scenario))
        for a in rwd_intpos_dic:
            for b in rwd_intpos_dic[a]:
                rewards_int_A[a][b] = round(
                    rewards_int_A[a][b] + learn_rate * (reward_apply - rewards_int_A[a][b]), 2)
    elif prev_scenario == "B":
        for a in rwd_intpos_dic:
            for b in rwd_intpos_dic[a]:
                rewards_int_B[a][b] = round(
                    rewards_int_B[a][b] + learn_rate * (reward_apply - rewards_int_B[a][b]), 2)
    elif prev_scenario == "C":
        for a in rwd_intpos_dic:
            for b in rwd_intpos_dic[a]:
                rewards_int_C[a][b] = round(
                    rewards_int_C[a][b] + learn_rate * (reward_apply - rewards_int_C[a][b]), 2)
    else:
        for a in rwd_intpos_dic:
            for b in rwd_intpos_dic[a]:
                rewards_int_D[a][b] = round(
                    rewards_int_D[a][b] + learn_rate * (reward_apply - rewards_int_D[a][b]), 2)


def check_to_int():
    if int_move_counter < int_step_allowance and into_int_state:
        return True
    return False


def game_reset():
    global game, act_move_counter, temp_dict_act, temp_dict_int, pos_act_rewards, pos_int_rewards, into_int_state
    game += 1
    act_move_counter = 0
    temp_dict_act = {}
    temp_dict_int = {}
    pos_act_rewards = {}
    pos_int_rewards = {}
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


while game < games:
    scenario = win_seq[game]
    # print("this is game number {} and the current scenario is {}".format(game, scenario))
    win_pos = set_win_pos(scenario)
    go_to_int = check_to_int()
    if go_to_int:
        # print("this is game number {} and the previous scenario for me is {} and current is {}".format(game, prev_scenario, scenario))
        int_action = pick_int_move(prev_scenario)
        # print("Game: {}  Current pos: {}  Next action: {}  State: interim".format(game + 1, current_pos, int_action))
        int_action_coord = int_action_trans[int_action]
        temp_dict_int = {current_pos: {int_action_coord: 0}}
        # print("Adding current position {}  with action {} to dic".format(current_pos, int_action_coord))
        dict_update(pos_int_rewards, temp_dict_int)
        current_pos = take_next_move(int_action)
        int_move_counter += 1
    else:
        into_int_state = False
        int_move_counter = 0
        if current_pos == win_pos:
            reward = base_reward - (act_move_counter * act_step_cost)
            # print(pos_act_rewards)
            update_act_rewards(pos_act_rewards, reward)
            update_int_rewards(pos_int_rewards, reward)
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
            temp_dict_act = {current_pos: {act_action_coord: 0}}
            dict_update(pos_act_rewards, temp_dict_act)
            current_pos = take_next_move(act_action)
            act_move_counter += 1

if rand_flag:
    print(" Random sequence used: {}".format(V))
    print(" Iterations: {}".format(iterations))
else:
    print(" Sequence used: {}".format(win_pattern))
    print(" Iterations: {}".format(iterations))


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Collecting data on trials
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AA_dic00 = minisquare_values(rewards_A, (0, 0))
AA_dic01 = minisquare_values(rewards_A, (0, 1))
AA_dic02 = minisquare_values(rewards_A, (0, 2))
AA_dic03 = minisquare_values(rewards_A, (0, 3))
AA_dic04 = minisquare_values(rewards_A, (0, 4))

AA_dic10 = minisquare_values(rewards_A, (1, 0))
AA_dic11 = minisquare_values(rewards_A, (1, 1))
AA_dic12 = minisquare_values(rewards_A, (1, 2))
AA_dic13 = minisquare_values(rewards_A, (1, 3))
AA_dic14 = minisquare_values(rewards_A, (1, 4))

AA_dic20 = minisquare_values(rewards_A, (2, 0))
AA_dic21 = minisquare_values(rewards_A, (2, 1))
AA_dic22 = minisquare_values(rewards_A, (2, 2))
AA_dic23 = minisquare_values(rewards_A, (2, 3))
AA_dic24 = minisquare_values(rewards_A, (2, 4))

AA_dic30 = minisquare_values(rewards_A, (3, 0))
AA_dic31 = minisquare_values(rewards_A, (3, 1))
AA_dic32 = minisquare_values(rewards_A, (3, 2))
AA_dic33 = minisquare_values(rewards_A, (3, 3))
AA_dic34 = minisquare_values(rewards_A, (3, 4))

AA_dic40 = minisquare_values(rewards_A, (4, 0))
AA_dic41 = minisquare_values(rewards_A, (4, 1))
AA_dic42 = minisquare_values(rewards_A, (4, 2))
AA_dic43 = minisquare_values(rewards_A, (4, 3))
AA_dic44 = minisquare_values(rewards_A, (4, 4))




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Visualizations
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# print(minisquare_values(rewards_A, (0, 0)))
# print(minisquare_values(rewards_A, (0, 1)))
# print(minisquare_values(rewards_A, (0, 2)))
# print(minisquare_values(rewards_A, (0, 3)))
# print(minisquare_values(rewards_A, (0, 4)))
#
# print(minisquare_values(rewards_A, (1, 0)))
# print(minisquare_values(rewards_A, (1, 1)))
# print(minisquare_values(rewards_A, (1, 2)))
# print(minisquare_values(rewards_A, (1, 3)))
# print(minisquare_values(rewards_A, (1, 4)))
#
# print(minisquare_values(rewards_A, (2, 0)))
# print(minisquare_values(rewards_A, (2, 1)))
# print(minisquare_values(rewards_A, (2, 2)))
# print(minisquare_values(rewards_A, (2, 3)))
# print(minisquare_values(rewards_A, (2, 4)))
#
# print(minisquare_values(rewards_A, (3, 0)))
# print(minisquare_values(rewards_A, (3, 1)))
# print(minisquare_values(rewards_A, (3, 2)))
# print(minisquare_values(rewards_A, (3, 3)))
# print(minisquare_values(rewards_A, (3, 4)))
#
# print(minisquare_values(rewards_A, (4, 0)))
# print(minisquare_values(rewards_A, (4, 1)))
# print(minisquare_values(rewards_A, (4, 2)))
# print(minisquare_values(rewards_A, (4, 3)))
# print(minisquare_values(rewards_A, (4, 4)))

minisquare_values(rewards_A, (1, 3))
minisquare_values(rewards_A, (1, 4))
minisquare_values(rewards_A, (0, 3))
minisquare_values(rewards_A, (0, 4))

minisquare_values(rewards_A, (1, 3))
minisquare_values(rewards_A, (1, 4))
minisquare_values(rewards_A, (0, 3))
minisquare_values(rewards_A, (0, 4))

minisquare_values(rewards_int_A, (0, 0))
minisquare_values(rewards_int_A, (2, 2))
minisquare_values(rewards_int_A, (0, 1))
minisquare_values(rewards_int_A, (1, 0))
#
# minisquare_values(rewards_int_B, (0, 4))
# minisquare_values(rewards_int_B, (2, 2))
# minisquare_values(rewards_int_B, (0, 3))
# minisquare_values(rewards_int_B, (1, 4))
#
# minisquare_values(rewards_int_C, (4, 0))
# minisquare_values(rewards_int_C, (2, 2))
# minisquare_values(rewards_int_C, (3, 0))
# minisquare_values(rewards_int_C, (4, 1))

# minisquare_values(rewards_post_D, (4, 4))
# minisquare_values(rewards_post_D, (2, 2))
# minisquare_values(rewards_post_D, (0, 0))
#
