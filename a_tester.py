import numpy as np
import random
import collections.abc


def test_model(testdic, testseq):
    into_int_state = False
    int_move_counter = 4
    act_move_counter = 1
    board_rows = 5
    board_cols = 5
    win_obj_A = (0, 0)
    win_obj_B = (0, 4)
    win_obj_C = (4, 0)
    win_obj_D = (4, 4)
    start_pos = (2, 2)
    current_pos = start_pos

    act_actions = [
        "up",
        "down",
        "left",
        "right",
        "uleft",
        "uright",
        "dleft",
        "dright",
        "stay"]
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
        0, 1), "uleft": (-1, -1), "uright": (-1, 1), "dleft": (1, -1), "dright": (1, 1), "stay": (0, 0)}
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

    def check_to_int():
        if int_move_counter < 4 and into_int_state:
            return True
        return False

    def pick_int_move(prev_target):
        next_int_action = ""
        random.shuffle(int_actions)
        best_reward = -1000000
        for a in int_actions:
            if prev_target == "A":
                poss_reward = testdic['Aint'][current_pos][int_action_trans[a]]
                if poss_reward > best_reward:
                    next_int_action = a
                    best_reward = poss_reward
            elif prev_target == "B":
                poss_reward = testdic['Bint'][current_pos][int_action_trans[a]]
                if poss_reward > best_reward:
                    next_int_action = a
                    best_reward = poss_reward
            elif prev_target == "C":
                poss_reward = testdic['Cint'][current_pos][int_action_trans[a]]
                if poss_reward > best_reward:
                    next_int_action = a
                    best_reward = poss_reward
            else:
                poss_reward = testdic['Dint'][current_pos][int_action_trans[a]]
                if poss_reward > best_reward:
                    next_int_action = a
                    best_reward = poss_reward
        return next_int_action

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

    test_seq = testseq
    games = len(test_seq)
    game = 0
    into_int_state = False

    while game < games:
        scenario = test_seq[game]
        win_pos = set_win_pos(scenario)
        go_to_int = check_to_int()
        if go_to_int:
            int_action = pick_int_move(prev_scenario)
            # if int_action == "":
            # todo: make it clear it got stuck here and end the game
            int_action_coord = int_action_trans[int_action]
            int_action_list.append((current_pos, int_action_coord))
            current_pos = take_next_move(int_action)
            int_move_counter += 1
            print("int move counter = {}".format(int_move_counter))
        else:
            into_int_state = False
            while into_int_state:
                int_lastpos = current_pos
                int_dist_test = int_distance_calc(int_lastpos, win_pos)
                int_dist_test_list.append(int_dist_test)
                into_int_state = False
            int_move_counter = 0
            if current_pos == win_pos:
                moves_per_test.append(act_move_counter)
                game_num_test.append(game + 1)
                scenario_per_test.append(scenario)
                game += 1
                act_move_counter = 0
                int_action_list = []
                act_action_list = []
                into_int_state = True
                prev_scenario = scenario
                print("game over")
            else:
                act_action = pick_act_move(scenario)
                # if check_testact_loop(act_action, current_pos):
                act_action_coord = act_action_trans[act_action]
                act_action_list.append((current_pos, act_action_coord))
                act_action_count(current_pos, act_action_coord, scenario)
                current_pos = take_next_move(act_action)
                print(current_pos)
                act_move_counter += 1
                print(act_move_counter)
                # todo: check if same square gets touched twice in testing, if so then end b/c endless loop
        # int_action = pick_int_move(prev_scenario)
        # int_action_coord = int_action_trans[int_action]
        # int_action_list.append((current_pos, int_action_coord))
        # int_action_count(current_pos, int_action_coord, prev_scenario)