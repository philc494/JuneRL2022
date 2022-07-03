import numpy as np
import random
import collections.abc

"""
Open questions:
- Resetting the position after each game?
- 
"""

# input desired paramters
win_seq = "AB" * 5
base_reward = 50
act_step_cost = 5
int_step_allowance = 4
exp_rate = 0.2
learn_rate = 0.3

# initialize starting variables
int_state_flag = True
into_int_state = True
int_move_counter = 0
act_move_counter = 1
games = len(win_seq)
game = 0
start_pos = (2, 2)
current_pos = start_pos
pos_act_rewards = {}
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

all_positions = []
for a in np.arange(0, 5):
    for b in np.arange(0, 5):
        all_positions.append((a, b))

all_actions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                   (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]

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


def check_to_int():
    if int_move_counter < int_step_allowance and into_int_state:
        return True
    return False


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


def pick_act_move(win_scenario):
    while True:
        random.shuffle(act_actions)
        next_act_action = ""
        if np.random.uniform(0, 1) <= exp_rate:
            next_act_action = np.random.choice(act_actions)
        else:
            best_reward = -1000000
            for a in act_actions:
                if win_scenario == "A":
                    poss_reward = rewards_A[take_next_move(
                        a)][act_action_trans[a]]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
                elif win_scenario == "B":
                    poss_reward = rewards_B[take_next_move(a)][act_action_trans[a]]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
                elif win_scenario == "C":
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


def dict_update(d, update):
    for k, v in update.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = dict_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d

  # for pos, actions in rwd_actpos_dic.items():
  #       for key in actions:


def update_rewards(rwd_actpos_dic, reward_apply):
    if scenario == "A":
        for a in rwd_actpos_dic:
            for b in rwd_actpos_dic[a]:
                rewards_A[a][b] = round(rewards_A[a][b] + learn_rate * (reward_apply - rewards_A[a][b]), 2)
    if scenario == "B":
        for a in rwd_actpos_dic:
            for b in rwd_actpos_dic[a]:
                rewards_B[a][b] = round(rewards_B[a][b] + learn_rate * (reward_apply - rewards_B[a][b]), 2)
    if scenario == "C":
        for a in rwd_actpos_dic:
            for b in rwd_actpos_dic[a]:
                rewards_C[a][b] = round(rewards_C[a][b] + learn_rate * (reward_apply - rewards_C[a][b]), 2)
    else:
        for a in rwd_actpos_dic:
            for b in rwd_actpos_dic[a]:
                rewards_D[a][b] = round(rewards_D[a][b] + learn_rate * (reward_apply - rewards_D[a][b]), 2)


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
    if reward_dic == rewards_A:
        z = "A"
        print("check1")
    elif reward_dic == rewards_B:
        z = "B"
        print("check2")
    elif reward_dic == rewards_C:
        z = "C"
        print("check3")
    elif reward_dic == rewards_D:
        z = "D"
        print("check4")
    else:
        z = "Z"
        print("check5")
    print(' {}--------------- Pos{} ---------------{}'.format(z, board_pos, z))
    for i in range(-1, 2):
        for j in range(-1, 2):
            mini_dic[(i, j)] = round((reward_dic[board_pos][(i, j)]), 1)
    for i in range(-1, 2):
        print(' -------------------------------------------')
        out = ' | '
        for j in range(-1, 2):
            out += str(float(mini_dic[(i, j)])).center(6) + '    |    '
        print(out)
    print(' {}--------------- Pos{} ---------------{}\n\n'.format(z, board_pos, z))


def game_reset():
    global game, act_move_counter, temp_dict, pos_act_rewards
    game += 1
    act_move_counter = 0
    temp_dict = {}
    pos_act_rewards = {}


while game < games:
    scenario = win_seq[game]
    win_pos = set_win_pos(scenario)
    go_to_int = check_to_int()
    if go_to_int:
        int_action = pick_int_move(scenario)
    if current_pos == win_pos:
        reward = base_reward - (act_move_counter * act_step_cost)
        update_rewards(pos_act_rewards, reward)
        print(
            "Game {} of {} completed:  Act moves in last game: {}".format(
                game + 1,
                games,
                act_move_counter - 1))
        game_reset()
    else:  # take another move in action state
        act_action = pick_act_move(scenario)
        print("Game: {}  Move #: {}  Current pos: {}  Action: {}  Target: {}".format(
            game + 1, act_move_counter, current_pos, act_action, win_pos))
        act_action_coord = act_action_trans[act_action]  # translate action into action coordinates
        temp_dict = {current_pos: {act_action_coord: 0}}
        dict_update(pos_act_rewards, temp_dict)
        current_pos = take_next_move(act_action)
        act_move_counter += 1


minisquare_values(rewards_A, (0, 1))
minisquare_values(rewards_A, (1, 0))
minisquare_values(rewards_D, (1, 0))

# todo: include entire interim state calculation and steps

