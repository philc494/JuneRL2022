import numpy as np
import random
import collections.abc

# input desired paramters
win_seq = "A" * 10
base_reward = 25
act_step_cost = .01 * base_reward
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
list_act_coords = []

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
int_action_trans = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),
                    "uleft": (-1, -1), "uright": (-1, 1), "dleft": (1, -1), "dright": (1, 1), "stay": (0, 0)}

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
inner_table = {}

rewards_positions = {}
rewards_positions_int = {}

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
        rewards_positions[(i, j)] = []

for i in range(-1, 2):
    for j in range(-1, 2):
        inner_table[i, j] = 0

for i in rewards_A:
    rewards_A[i] = inner_table
for i in rewards_B:
    rewards_B[i] = inner_table
for i in rewards_C:
    rewards_C[i] = inner_table
for i in rewards_D:
    rewards_D[i] = inner_table
for i in rewards_int_A:
    rewards_int_A[i] = inner_table
for i in rewards_int_B:
    rewards_int_B[i] = inner_table
for i in rewards_int_C:
    rewards_int_C[i] = inner_table
for i in rewards_int_D:
    rewards_int_D[i] = inner_table


# takes a letter for the win scenario and returns the win position
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


# takes a direction and returns a new position (or current pos if move is
# illegal)
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

d_new = {}
position_list = []
action_list = []

# choose move to enact either randomly or using best available next move
def pick_act_move(win_scenario):
    while True:
        # prevent choosing last action in list by default every time in
        # beginning
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
                # elif win_scenario == "B":
                #     poss_reward = rewards_B[take_next_move(a)]
                #     if poss_reward > best_reward:
                #         next_act_action = a
                #         best_reward = poss_reward
                # elif win_scenario == "C":
                #     poss_reward = rewards_C[take_next_move(a)]
                #     if poss_reward > best_reward:
                #         next_act_action = a
                #         best_reward = poss_reward
                # else:
                #     poss_reward = rewards_D[take_next_move(a)]
                #     if poss_reward > best_reward:
                #         next_act_action = a
                #         best_reward = poss_reward
        new_position = take_next_move(next_act_action)
        if new_position == current_pos:
            continue
        else:
            return next_act_action


def dict_update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = dict_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


master = {}
while game < games:
    scenario = win_seq[game]
    win_pos = set_win_pos(scenario)
    if current_pos == win_pos:
        reward = base_reward - (act_move_counter * act_step_cost)
        if scenario == "A":
            for a in rewards_positions:
                end_reward = a[b] + learn_rate * (reward - a[b])
                rewards_A[a][b] = round(end_reward, 2)
        print(
            "Game {} of {} completed:  Act moves in last game: {}".format(
                game + 1,
                games,
                act_move_counter))
        game += 1
        act_move_counter = 0
    else:  # take another move in action state
        position_list.append(current_pos)
        act_action = pick_act_move(scenario)
        print("Game: {}  Move #: {}  Current pos: {}  Action: {}  Target: {}".format(
            game + 1, act_move_counter, current_pos, act_action, win_pos))
        act_action_coord = act_action_trans[act_action]  # translate action into action coordinates
        temp = {current_pos: {act_action_coord: 0}}
        dict_update(master, temp)
        print(master)
        current_pos = take_next_move(act_action)
        act_move_counter += 1





    # rewards_positions[current_pos] = {act_action_coord: 0}

    # go_to_int = check_to_int()
    # if go_to_int:
    #     int_action = pick_int_move()
# show_values()  # todo: funciton to show values based on tables used
