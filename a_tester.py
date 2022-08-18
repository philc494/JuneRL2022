import numpy as np
import random
import collections.abc


def test_model(testdic, testseq, model):
    int_move_counter = 0
    act_move_counter = 0
    board_rows = 5
    board_cols = 5
    win_obj_A = (0, 0)
    win_obj_B = (0, 4)
    win_obj_C = (4, 0)
    win_obj_D = (4, 4)
    start_pos = (2, 2)

    dist_recorded = False
    int_action_list = []
    act_action_list = []
    moves_per_test = []
    game_num_test = []
    scenario_per_test = []
    test_dist_list = []

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
        if prev_target == "A":
            for a in int_actions:
                poss_reward = testdic['Aint'][current_pos][int_action_trans[a]]
                if poss_reward > best_reward:
                    next_int_action = a
                    best_reward = poss_reward
        elif prev_target == "B":
            for a in int_actions:
                poss_reward = testdic['Bint'][current_pos][int_action_trans[a]]
                if poss_reward > best_reward:
                    next_int_action = a
                    best_reward = poss_reward
        elif prev_target == "C":
            for a in int_actions:
                poss_reward = testdic['Cint'][current_pos][int_action_trans[a]]
                if poss_reward > best_reward:
                    next_int_action = a
                    best_reward = poss_reward
        else:
            for a in int_actions:
                poss_reward = testdic['Dint'][current_pos][int_action_trans[a]]
                if poss_reward > best_reward:
                    next_int_action = a
                    best_reward = poss_reward
        return next_int_action

    def pick_act_move(win_target):
        next_act_action = ""
        while True:
            random.shuffle(act_actions)
            best_reward = -1000000
            if win_target == "A":
                for a in act_actions:
                    poss_reward = testdic['A'][current_pos][act_action_trans[a]]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
            elif win_target == "B":
                for a in act_actions:
                    poss_reward = testdic['B'][current_pos][act_action_trans[a]]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
            elif win_target == "C":
                for a in act_actions:
                    poss_reward = testdic['C'][current_pos][act_action_trans[a]]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
            else:
                for a in act_actions:
                    poss_reward = testdic['D'][current_pos][act_action_trans[a]]
                    if poss_reward > best_reward:
                        next_act_action = a
                        best_reward = poss_reward
            return next_act_action

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

    def dist_calc(currentpos, next_target):
        if next_target == 'A':
            dist = max(abs(currentpos[0] - win_obj_A[0]), abs(currentpos[1] - win_obj_A[1]))
        elif next_target == 'B':
            dist = max(abs(currentpos[0] - win_obj_B[0]), abs(currentpos[1] - win_obj_B[1]))
        elif next_target == 'C':
            dist = max(abs(currentpos[0] - win_obj_C[0]), abs(currentpos[1] - win_obj_C[1]))
        else:
            dist = max(abs(currentpos[0] - win_obj_D[0]), abs(currentpos[1] - win_obj_D[1]))
        return dist

    test_seq = testseq
    games = len(test_seq)
    game = 0
    prev_scenario = test_seq[-1]

    current_pos = win_obj_B
    into_int_state = True

    while game < games:
        scenario = test_seq[game]
        win_pos = set_win_pos(scenario)
        go_to_int = check_to_int()
        if go_to_int:
            int_action = pick_int_move(prev_scenario)
            int_action_coord = int_action_trans[int_action]
            int_action_list.append((current_pos, int_action_coord))
            current_pos = take_next_move(int_action)
            print("Testing model {}: new int position following scenario {} is {}".format(model,
                                                                                          prev_scenario, current_pos))
            int_move_counter += 1
        else:
            into_int_state = False
            if not dist_recorded:
                int_distance = dist_calc(current_pos, scenario)
                test_dist_list.append(int_distance)
                dist_recorded = True
            if current_pos == win_pos:
                moves_per_test.append(act_move_counter)
                game_num_test.append(game + 1)
                scenario_per_test.append(scenario)
                print("Game over for scenario {}".format(scenario))
                game += 1
                act_move_counter = 0
                int_move_counter = 0
                int_action_list = []
                act_action_list = []
                into_int_state = True
                dist_recorded = False
                prev_scenario = scenario
            else:
                act_action = pick_act_move(scenario)
                act_action_coord = act_action_trans[act_action]
                act_action_list.append((current_pos, act_action_coord))
                current_pos = take_next_move(act_action)
                print("Testing model {}: new action position targeting scenario {} is {}".format(model,
                                                                                                 scenario, current_pos))
                act_move_counter += 1

    info_return = {'test_moves': moves_per_test, 'games_test': game_num_test,
                   'scen_test': scenario_per_test, 'test_dist': test_dist_list}
    print("Model {} test: complete".format(model))
    return info_return
