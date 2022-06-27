import numpy as np

# Board initialization and rules
board_rows = 5
board_cols = 5
board = np.zeros([board_rows, board_cols])

win_obj_A = (0, 0)
win_obj_B = (0, 4)
win_obj_C = (4, 0)
win_obj_D = (4, 4)

# Reward tables - initialize to zero

rewards_A = {}
rewards_B = {}
rewards_C = {}
rewards_D = {}
rewards_int = {}

for i in range(board_rows):
    for j in range(board_cols):
        rewards_A[(i, j)] = 0
        rewards_B[(i, j)] = 0
        rewards_C[(i, j)] = 0
        rewards_D[(i, j)] = 0
        rewards_int[(i, j)] = 0

win_seq = "ABCDAABCDAABCDAABCDAABCDAABCDAABCDAABCDAABCDAABCDA"  # Current sequence: 10x "ABCDA"
games = len(win_seq)

start_pos = (2, 2)
current_pos = start_pos

act_actions = ["up", "down", "left", "right", "uleft", "uright", "dleft", "dright"]
int_actions = ["up", "down", "left", "right", "uleft", "uright", "dleft", "dright", "stay"]


int_step_allowance = 0
int_steps_remaining = 0
int_state_flag = True

exp_rate = 0.2
learn_rate = 0.2


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


def check_act_done():
    if win_pos == current_pos:
        return True
    return False


def pick_int_move(): # Looks at all possible moves; chooses random or best; returns action ("Up")
    best_reward = 0
    poss_reward = 0
    next_int_action = ""
    if np.random.uniform(0, 1) <= exp_rate:
        next_int_action = np.random.choice(int_actions)
    else:
        for a in int_actions:
            poss_reward = rewards_int[take_next_move(a)]
            if poss_reward >= best_reward:
                next_int_action = a
                best_reward = poss_reward
    return next_int_action

def take_int_move(chosen_int_action): # Takes an action; returns new position (if action is legal)
    next_int_position = take_next_move(chosen_int_action)
    return next_int_position

# def check_int_done():
#     if win_pos == current_pos:
#         return True
#     return False


i = 0
while i < games:
    if int_state_flag:
        int_action = pick_int_move() # gives "Up"
         = take_int_move(int_action) # changes position



    scenario = win_seq[i]
    win_pos = set_win_pos(scenario)

    # choose interim steps
    # how to make interim only happen once??
    # if not already to target, jump to taking more moves
    # if to target, update all relevant values and reset the game

    act_state_end = check_act_done()



    if act_state_end:


        if int_steps_remaining == 0:

            int_state_flag = True
            pass
    else:
        # decide move
        # take move
        pass
