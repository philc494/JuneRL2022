import numpy as np
import random
"""
Open questions so far:
# Should interim steps receive movement penalty given they are forced? Currently not
# Should action mode steps that are illegal count as a move / have a cost? Currently no - built so it must move each time
# Unexplained behavior:
 - why does higher step cost cause the model to run significantly longer?
 - why does it still take so long to play certain games?
 - why is there always another corner with almost as much reward as the Target?
 # to fix/improve:
 - visualization / formatting with large numbers
 
 Ideas:
 - random position values to start - slight differences - heuristic (-1 to 1)
 - Q table with 8 values for each position (not corners)
    - inside each square is a set of smaller squares
    - function to prepare results for entire model
    - best position = draw as a line
    - xy within xy 
    - number that changes first should change first conceptually
    - next: different interim tables for each scenario
        - interim: can it learn ABCDABAD... repeated
 
 
"""
# initialize starting variables
int_state_flag = True
into_int_state = True
int_move_counter = 0
act_move_counter = 1
start_pos = (2, 2)
current_pos = start_pos
game = 0

# input desired win sequence
win_seq = "ABAAAAA" * 50
games = len(win_seq)

# input desired exploration and learning rate
exp_rate = 0.2
learn_rate = 0.3

# input desired base reward and movement cost
base_reward = 25
act_step_cost = .01 * base_reward

# allowed actions by state
act_actions = ["up", "down", "left", "right", "uleft", "uright", "dleft", "dright"]
int_actions = ["up", "down", "left", "right", "uleft", "uright", "dleft", "dright", "stay"]

int_step_allowance = 4

# board initialization and rules
board_rows = 5
board_cols = 5
board = {}
int_board = {}
for i in range(board_rows):
    for j in range(board_cols):
        board[(i, j)] = 0

# set locations of win scenarios and initialize separate reward tables to 0
win_obj_A = (0, 0)
win_obj_B = (0, 4)
win_obj_C = (4, 0)
win_obj_D = (4, 4)

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

# single list for storing positions to receive rewards after each episode
reward_positions = []
int_reward_positions = []


"""
Functions used
"""


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


# takes a direction and returns a new position (or current pos if move is illegal)
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


# choose move to enact either randomly or using best available next move
def pick_act_move(win_scenario):
    while True:
        random.shuffle(act_actions)  # prevent choosing last action in list by default every time in beginning
        next_act_action = ""
        if np.random.uniform(0, 1) <= exp_rate:
            next_act_action = np.random.choice(act_actions)
        else:
            best_reward = -1000000
            for a in act_actions:
                if win_scenario == "A":
                    poss_reward = rewards_A[take_next_move(a)]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
                elif win_scenario == "B":
                    poss_reward = rewards_B[take_next_move(a)]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
                elif win_scenario == "C":
                    poss_reward = rewards_C[take_next_move(a)]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
                else:
                    poss_reward = rewards_D[take_next_move(a)]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
        new_position = take_next_move(next_act_action)
        if new_position == current_pos:
            print("Tried {} but I remain stuck in {} as of move {}".format(next_act_action, current_pos, act_move_counter))
            continue
        else:
            return next_act_action


# looks at all possible moves; chooses random or best; returns action ("Up")
def pick_int_move():
    while True:
        best_reward = 0
        next_int_action = ""
        random.shuffle(int_actions)
        if np.random.uniform(0, 1) <= exp_rate:
            next_int_action = np.random.choice(int_actions)
        else:
            for a in int_actions:
                poss_reward = rewards_int[take_next_move(a)]
                if poss_reward >= best_reward:
                    next_int_action = a
                    best_reward = poss_reward
        new_position = take_next_move(next_int_action)
        if new_position == current_pos and next_int_action != "stay":
            continue
        return next_int_action


def show_int_board():
    for i in range(board_rows):
        for j in range(board_cols):
            int_board[(i, j)] = "o"
    for a in int_board:
        for z in int_reward_positions:
            if a == z:
                int_board[a] = "!!"
    for i in range(0, board_rows):
        print('--------------------------')
        out = '| '
        for j in range(0, board_cols):
            out += str(int_board[(i, j)]).ljust(2) + ' | '
        print(out)
    print('--------------------------')


# checks if the interim state is done yet
def check_to_int():
    if int_move_counter == int_step_allowance:
        show_int_board()
    if int_move_counter < int_step_allowance and into_int_state:
        return True
    return False


# print reward values for the respective scenario
def show_values(letter):
    print('------Reward Table {} for Game {}-------'.format(letter, games))
    for i in range(0, board_rows):
        print('-----------------------------------------')
        out = '| '
        for j in range(0, board_cols):
            if letter == "A":
                out += str(rewards_A[(i, j)]).ljust(5) + ' | '
            elif letter == "B":
                out += str(rewards_B[(i, j)]).ljust(5) + ' | '
            elif letter == "C":
                out += str(rewards_C[(i, j)]).ljust(5) + ' | '
            elif letter == "D":
                out += str(rewards_D[(i, j)]).ljust(5) + ' | '
            else:
                out += str(rewards_int[(i, j)]).ljust(5) + ' | '
        print(out)
    print('-----------------------------------------')


"""
End of initialization & functions
"""

# main script
while game < games:
    scenario = win_seq[game]
    win_pos = set_win_pos(scenario)
    go_to_int = check_to_int()
    if go_to_int:  # if still in interim state
        int_action = pick_int_move()  # gives "Up"
        print("Game: {}  New pos: {}  Next action: {}  State: interim".format(game + 1, current_pos, int_action))
        current_pos = take_next_move(int_action)  # changes position
        int_reward_positions.append(current_pos)  # add interim position to list to be rewarded
        int_move_counter += 1
    else:  # if goal reached, reward specific reward table (+ int table) and reset
        into_int_state = False
        int_move_counter = 0
        if current_pos == win_pos:
            reward = base_reward - (act_move_counter * act_step_cost)
            if scenario == "A":
                for s in set(reversed(reward_positions)):  # use "set" to include only unique values; back propogate
                    end_reward = rewards_A[s] + learn_rate * (reward - rewards_A[s])
                    rewards_A[s] = round(end_reward, 2)
                for s in set(reversed(int_reward_positions)):
                    end_reward = rewards_int[s] + learn_rate * (reward - rewards_int[s])
                    rewards_int[s] = round(end_reward, 2)
            elif scenario == "B":
                for s in set(reversed(reward_positions)):
                    end_reward = rewards_B[s] + learn_rate * (reward - rewards_B[s])
                    rewards_B[s] = round(end_reward, 2)
                for s in set(reversed(int_reward_positions)):
                    end_reward = rewards_int[s] + learn_rate * (reward - rewards_int[s])
                    rewards_int[s] = round(end_reward, 2)
            elif scenario == "C":
                for s in set(reversed(reward_positions)):
                    end_reward = rewards_C[s] + learn_rate * (reward - rewards_C[s])
                    rewards_C[s] = round(end_reward, 2)
                for s in set(reversed(int_reward_positions)):
                    end_reward = rewards_int[s] + learn_rate * (reward - rewards_int[s])
                    rewards_int[s] = round(end_reward, 2)
            else:
                for s in set(reversed(reward_positions)):
                    end_reward = rewards_D[s] + learn_rate * (reward - rewards_D[s])
                    rewards_D[s] = round(end_reward, 2)
                for s in set(reversed(int_reward_positions)):
                    end_reward = rewards_int[s] + learn_rate * (reward - rewards_int[s])
                    rewards_int[s] = round(end_reward, 2)
            print("Game {} of {} completed:  Act moves in last game: {}".format(game + 1, games, act_move_counter))
            show_values("A")
            show_values("B")
            # show_values("C")
            # show_values("D")
            game += 1
            act_move_counter = 0
            reward_positions = []
            int_reward_positions = []
            into_int_state = True
        else:  # take another move in action state
            act_action = pick_act_move(scenario)
            print("Game: {}  Target: {}  New pos: {}  Next action: {}  Move #: {}".format(game + 1, win_pos, current_pos, act_action, act_move_counter + 1))
            current_pos = take_next_move(act_action)
            reward_positions.append(take_next_move(act_action))
            act_move_counter += 1

show_values("int")

