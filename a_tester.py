import numpy as np
import random
import collections.abc

AA_trans = 0
AB_trans = 0
AC_trans = 0
AD_trans = 0
Amid_trans = 0
Aup_trans = 0
Adown_trans = 0
Aleft_trans = 0
Aright_trans = 0

BA_trans = 0
BB_trans = 0
BC_trans = 0
BD_trans = 0
Bmid_trans = 0
Bup_trans = 0
Bdown_trans = 0
Bleft_trans = 0
Bright_trans = 0

CA_trans = 0
CB_trans = 0
CC_trans = 0
CD_trans = 0
Cmid_trans = 0
Cup_trans = 0
Cdown_trans = 0
Cleft_trans = 0
Cright_trans = 0

DA_trans = 0
DB_trans = 0
DC_trans = 0
DD_trans = 0
Dmid_trans = 0
Dup_trans = 0
Ddown_trans = 0
Dleft_trans = 0
Dright_trans = 0


def test_model(testdic, testseq, model, parameters):
    global AA_trans, AB_trans, AC_trans, AD_trans, Amid_trans, Aup_trans, Adown_trans, Aleft_trans, \
        Aright_trans, BA_trans, BB_trans, BC_trans, BD_trans, Bmid_trans, Bup_trans, Bdown_trans, \
        Bleft_trans, Bright_trans, CA_trans, CB_trans, CC_trans, CD_trans, Cmid_trans, Cup_trans, \
        Cdown_trans, Cleft_trans, Cright_trans, DA_trans, DB_trans, DC_trans, DD_trans, Dmid_trans, \
        Dup_trans, Ddown_trans, Dleft_trans, Dright_trans
    exp_rate = parameters['exp_rate']
    int_move_counter = 0
    act_move_counter = 0
    board_rows = 5
    board_cols = 5
    win_obj_A = (0, 0)
    win_obj_B = (0, 4)
    win_obj_C = (4, 0)
    win_obj_D = (4, 4)

    dist_recorded = False
    int_action_list = []
    act_action_list = []
    moves_per_test = []
    game_num_test = []
    scenario_per_test = []
    test_dist_list = []
    int_final_list = []
    int_scenario_list = []

    A_squares = [(0, 0), (0, 1), (1, 0), (1, 1)]
    B_squares = [(0, 4), (0, 3), (1, 3), (1, 4)]
    C_squares = [(4, 0), (3, 0), (4, 1), (3, 1)]
    D_squares = [(4, 4), (4, 3), (3, 4), (3, 3)]
    mid_square = [(2, 2)]
    up_cross = [(0, 2), (1, 2)]
    down_cross = [(3, 2), (4, 2)]
    left_cross = [(2, 0), (2, 1)]
    right_cross = [(2, 3), (2, 4)]

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
        if model == 2:
            next_int_action = ""
            while True:
                random.shuffle(int_actions)
                if np.random.uniform(0, 1) <= exp_rate:
                    next_int_action = np.random.choice(int_actions)
                else:
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
                new_position = take_next_move(next_int_action)
                if new_position == current_pos and next_int_action != "stay":
                    continue
                else:
                    return next_int_action
        elif model == 1:
            while True:
                int_rewards = []
                if prev_target == "A":
                    up_reward = testdic['Aint'][current_pos][act_action_trans['up']]
                    down_reward = testdic['Aint'][current_pos][act_action_trans['down']]
                    left_reward = testdic['Aint'][current_pos][act_action_trans['left']]
                    right_reward = testdic['Aint'][current_pos][act_action_trans['right']]
                    uleft_reward = testdic['Aint'][current_pos][act_action_trans['uleft']]
                    uright_reward = testdic['Aint'][current_pos][act_action_trans['uright']]
                    dleft_reward = testdic['Aint'][current_pos][act_action_trans['dleft']]
                    dright_reward = testdic['Aint'][current_pos][act_action_trans['dright']]
                    stay_reward = testdic['Aint'][current_pos][act_action_trans['stay']]
                    int_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                        uleft_reward, uright_reward, dleft_reward, dright_reward,
                                        stay_reward])
                    next_int_action = random.choices(int_actions, weights=(up_reward ** 2, down_reward ** 2,
                                                                           left_reward ** 2, right_reward ** 2,
                                                                           uleft_reward ** 2, uright_reward ** 2,
                                                                           dleft_reward ** 2, dright_reward ** 2,
                                                                           stay_reward ** 2), k=1)[0]
                elif prev_target == "B":
                    up_reward = testdic['Bint'][current_pos][act_action_trans['up']]
                    down_reward = testdic['Bint'][current_pos][act_action_trans['down']]
                    left_reward = testdic['Bint'][current_pos][act_action_trans['left']]
                    right_reward = testdic['Bint'][current_pos][act_action_trans['right']]
                    uleft_reward = testdic['Bint'][current_pos][act_action_trans['uleft']]
                    uright_reward = testdic['Bint'][current_pos][act_action_trans['uright']]
                    dleft_reward = testdic['Bint'][current_pos][act_action_trans['dleft']]
                    dright_reward = testdic['Bint'][current_pos][act_action_trans['dright']]
                    stay_reward = testdic['Bint'][current_pos][act_action_trans['stay']]
                    int_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                        uleft_reward, uright_reward, dleft_reward, dright_reward,
                                        stay_reward])
                    next_int_action = random.choices(int_actions, weights=(up_reward ** 2, down_reward ** 2,
                                                                           left_reward ** 2, right_reward ** 2,
                                                                           uleft_reward ** 2, uright_reward ** 2,
                                                                           dleft_reward ** 2, dright_reward ** 2,
                                                                           stay_reward ** 2), k=1)[0]
                elif prev_target == "C":
                    up_reward = testdic['Cint'][current_pos][act_action_trans['up']]
                    down_reward = testdic['Cint'][current_pos][act_action_trans['down']]
                    left_reward = testdic['Cint'][current_pos][act_action_trans['left']]
                    right_reward = testdic['Cint'][current_pos][act_action_trans['right']]
                    uleft_reward = testdic['Cint'][current_pos][act_action_trans['uleft']]
                    uright_reward = testdic['Cint'][current_pos][act_action_trans['uright']]
                    dleft_reward = testdic['Cint'][current_pos][act_action_trans['dleft']]
                    dright_reward = testdic['Cint'][current_pos][act_action_trans['dright']]
                    stay_reward = testdic['Cint'][current_pos][act_action_trans['stay']]
                    int_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                        uleft_reward, uright_reward, dleft_reward, dright_reward,
                                        stay_reward])
                    next_int_action = random.choices(int_actions, weights=(up_reward ** 2, down_reward ** 2,
                                                                           left_reward ** 2, right_reward ** 2,
                                                                           uleft_reward ** 2, uright_reward ** 2,
                                                                           dleft_reward ** 2, dright_reward ** 2,
                                                                           stay_reward ** 2), k=1)[0]
                else:
                    up_reward = testdic['Dint'][current_pos][act_action_trans['up']]
                    down_reward = testdic['Dint'][current_pos][act_action_trans['down']]
                    left_reward = testdic['Dint'][current_pos][act_action_trans['left']]
                    right_reward = testdic['Dint'][current_pos][act_action_trans['right']]
                    uleft_reward = testdic['Dint'][current_pos][act_action_trans['uleft']]
                    uright_reward = testdic['Dint'][current_pos][act_action_trans['uright']]
                    dleft_reward = testdic['Dint'][current_pos][act_action_trans['dleft']]
                    dright_reward = testdic['Dint'][current_pos][act_action_trans['dright']]
                    stay_reward = testdic['Dint'][current_pos][act_action_trans['stay']]
                    int_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                        uleft_reward, uright_reward, dleft_reward, dright_reward,
                                        stay_reward])
                    next_int_action = random.choices(int_actions, weights=(up_reward ** 2, down_reward ** 2,
                                                                           left_reward ** 2, right_reward ** 2,
                                                                           uleft_reward ** 2, uright_reward ** 2,
                                                                           dleft_reward ** 2, dright_reward ** 2,
                                                                           stay_reward ** 2), k=1)[0]
                new_position = take_next_move(next_int_action)
                if new_position == current_pos and next_int_action != "stay":
                    continue
                else:
                    return next_int_action

    def pick_act_move(win_target):
        if model == 2:
            next_act_action = ""
            while True:
                random.shuffle(act_actions)
                if np.random.uniform(0, 1) <= exp_rate:
                    next_act_action = np.random.choice(act_actions)
                else:
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
                new_position = take_next_move(next_act_action)
                if new_position == current_pos and next_act_action != "stay":
                    continue
                else:
                    return next_act_action
        if model == 1:
            while True:
                act_rewards = []
                if win_target == "A":
                    up_reward = testdic['A'][current_pos][act_action_trans['up']]
                    down_reward = testdic['A'][current_pos][act_action_trans['down']]
                    left_reward = testdic['A'][current_pos][act_action_trans['left']]
                    right_reward = testdic['A'][current_pos][act_action_trans['right']]
                    uleft_reward = testdic['A'][current_pos][act_action_trans['uleft']]
                    uright_reward = testdic['A'][current_pos][act_action_trans['uright']]
                    dleft_reward = testdic['A'][current_pos][act_action_trans['dleft']]
                    dright_reward = testdic['A'][current_pos][act_action_trans['dright']]
                    stay_reward = testdic['A'][current_pos][act_action_trans['stay']]
                    act_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                        uleft_reward, uright_reward, dleft_reward, dright_reward,
                                        stay_reward])
                    next_act_action = random.choices(act_actions, weights=(up_reward ** 2, down_reward ** 2,
                                                                           left_reward ** 2, right_reward ** 2,
                                                                           uleft_reward ** 2, uright_reward ** 2,
                                                                           dleft_reward ** 2, dright_reward ** 2,
                                                                           stay_reward ** 2), k=1)[0]

                elif win_target == "B":
                    up_reward = testdic['B'][current_pos][act_action_trans['up']]
                    down_reward = testdic['B'][current_pos][act_action_trans['down']]
                    left_reward = testdic['B'][current_pos][act_action_trans['left']]
                    right_reward = testdic['B'][current_pos][act_action_trans['right']]
                    uleft_reward = testdic['B'][current_pos][act_action_trans['uleft']]
                    uright_reward = testdic['B'][current_pos][act_action_trans['uright']]
                    dleft_reward = testdic['B'][current_pos][act_action_trans['dleft']]
                    dright_reward = testdic['B'][current_pos][act_action_trans['dright']]
                    stay_reward = testdic['B'][current_pos][act_action_trans['stay']]
                    act_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                        uleft_reward, uright_reward, dleft_reward, dright_reward,
                                        stay_reward])
                    next_act_action = random.choices(act_actions, weights=(up_reward ** 2, down_reward ** 2,
                                                                           left_reward ** 2, right_reward ** 2,
                                                                           uleft_reward ** 2, uright_reward ** 2,
                                                                           dleft_reward ** 2, dright_reward ** 2,
                                                                           stay_reward ** 2), k=1)[0]
                elif win_target == "C":
                    up_reward = testdic['C'][current_pos][act_action_trans['up']]
                    down_reward = testdic['C'][current_pos][act_action_trans['down']]
                    left_reward = testdic['C'][current_pos][act_action_trans['left']]
                    right_reward = testdic['C'][current_pos][act_action_trans['right']]
                    uleft_reward = testdic['C'][current_pos][act_action_trans['uleft']]
                    uright_reward = testdic['C'][current_pos][act_action_trans['uright']]
                    dleft_reward = testdic['C'][current_pos][act_action_trans['dleft']]
                    dright_reward = testdic['C'][current_pos][act_action_trans['dright']]
                    stay_reward = testdic['C'][current_pos][act_action_trans['stay']]
                    act_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                        uleft_reward, uright_reward, dleft_reward, dright_reward,
                                        stay_reward])
                    next_act_action = random.choices(act_actions, weights=(up_reward ** 2, down_reward ** 2,
                                                                           left_reward ** 2, right_reward ** 2,
                                                                           uleft_reward ** 2, uright_reward ** 2,
                                                                           dleft_reward ** 2, dright_reward ** 2,
                                                                           stay_reward ** 2), k=1)[0]
                else:
                    up_reward = testdic['D'][current_pos][act_action_trans['up']]
                    down_reward = testdic['D'][current_pos][act_action_trans['down']]
                    left_reward = testdic['D'][current_pos][act_action_trans['left']]
                    right_reward = testdic['D'][current_pos][act_action_trans['right']]
                    uleft_reward = testdic['D'][current_pos][act_action_trans['uleft']]
                    uright_reward = testdic['D'][current_pos][act_action_trans['uright']]
                    dleft_reward = testdic['D'][current_pos][act_action_trans['dleft']]
                    dright_reward = testdic['D'][current_pos][act_action_trans['dright']]
                    stay_reward = testdic['D'][current_pos][act_action_trans['stay']]
                    act_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                        uleft_reward, uright_reward, dleft_reward, dright_reward,
                                        stay_reward])
                    next_act_action = random.choices(act_actions, weights=(up_reward ** 2, down_reward ** 2,
                                                                           left_reward ** 2, right_reward ** 2,
                                                                           uleft_reward ** 2, uright_reward ** 2,
                                                                           dleft_reward ** 2, dright_reward ** 2,
                                                                           stay_reward ** 2), k=1)[0]
                new_position = take_next_move(next_act_action)
                if new_position == current_pos and next_act_action != "stay":
                    continue
                else:
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

    def categorize_intsquare(finalintpos, prevscen):
        global AA_trans, AB_trans, AC_trans, AD_trans, Amid_trans, Aup_trans, Adown_trans, Aleft_trans, \
            Aright_trans, BA_trans, BB_trans, BC_trans, BD_trans, Bmid_trans, Bup_trans, Bdown_trans, \
            Bleft_trans, Bright_trans, CA_trans, CB_trans, CC_trans, CD_trans, Cmid_trans, Cup_trans, \
            Cdown_trans, Cleft_trans, Cright_trans, DA_trans, DB_trans, DC_trans, DD_trans, Dmid_trans, \
            Dup_trans, Ddown_trans, Dleft_trans, Dright_trans
        if prevscen == "A":
            if finalintpos in A_squares:
                AA_trans += 1
            elif finalintpos in B_squares:
                AB_trans += 1
            elif finalintpos in C_squares:
                AC_trans += 1
            elif finalintpos in D_squares:
                AD_trans += 1
            elif finalintpos in mid_square:
                Amid_trans += 1
            elif finalintpos in up_cross:
                Aup_trans += 1
            elif finalintpos in down_cross:
                Adown_trans += 1
            elif finalintpos in left_cross:
                Aleft_trans += 1
            else:
                Aright_trans += 1
        elif prevscen == "B":
            if finalintpos in A_squares:
                BA_trans += 1
            elif finalintpos in B_squares:
                BB_trans += 1
            elif finalintpos in C_squares:
                BC_trans += 1
            elif finalintpos in D_squares:
                BD_trans += 1
            elif finalintpos in mid_square:
                Bmid_trans += 1
            elif finalintpos in up_cross:
                Bup_trans += 1
            elif finalintpos in down_cross:
                Bdown_trans += 1
            elif finalintpos in left_cross:
                Bleft_trans += 1
            else:
                Bright_trans += 1
        elif prevscen == "C":
            if finalintpos in A_squares:
                CA_trans += 1
            elif finalintpos in B_squares:
                CB_trans += 1
            elif finalintpos in C_squares:
                CC_trans += 1
            elif finalintpos in D_squares:
                CD_trans += 1
            elif finalintpos in mid_square:
                Cmid_trans += 1
            elif finalintpos in up_cross:
                Cup_trans += 1
            elif finalintpos in down_cross:
                Cdown_trans += 1
            elif finalintpos in left_cross:
                Cleft_trans += 1
            else:
                Cright_trans += 1
        else:
            if finalintpos in A_squares:
                DA_trans += 1
            elif finalintpos in B_squares:
                DB_trans += 1
            elif finalintpos in C_squares:
                DC_trans += 1
            elif finalintpos in D_squares:
                DD_trans += 1
            elif finalintpos in mid_square:
                Dmid_trans += 1
            elif finalintpos in up_cross:
                Dup_trans += 1
            elif finalintpos in down_cross:
                Ddown_trans += 1
            elif finalintpos in left_cross:
                Dleft_trans += 1
            else:
                Dright_trans += 1

    test_seq = testseq
    games = len(test_seq)
    game = 0
    prev_scenario = test_seq[-1]
    if prev_scenario == "A":
        current_pos = win_obj_A
    elif prev_scenario == "B":
        current_pos = win_obj_B
    elif prev_scenario == "C":
        current_pos = win_obj_C
    else:
        current_pos = win_obj_D
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
                categorize_intsquare(current_pos, prev_scenario)
                int_scenario_list.append(prev_scenario)
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

    def calc_prob(xxprob, xx1, xx2, xx3, xx4, xx5, xx6, xx7, xx8, xx9):
        try:
            prob = xxprob / (xx1 + xx2 + xx3 + xx4 + xx5 + xx6 + xx7 + xx8 + xx9)
            return prob
        except ZeroDivisionError:
            return 0

    AA_tp = calc_prob(AA_trans, AA_trans, AB_trans, AC_trans, AD_trans, Amid_trans,
                      Aleft_trans, Aup_trans, Adown_trans, Aright_trans)

    AB_tp = calc_prob(AB_trans, AA_trans, AB_trans, AC_trans, AD_trans, Amid_trans,
                      Aleft_trans, Aup_trans, Adown_trans, Aright_trans)

    AC_tp = calc_prob(AC_trans, AA_trans, AB_trans, AC_trans, AD_trans, Amid_trans,
                      Aleft_trans, Aup_trans, Adown_trans, Aright_trans)

    AD_tp = calc_prob(AD_trans, AA_trans, AB_trans, AC_trans, AD_trans, Amid_trans,
                      Aleft_trans, Aup_trans, Adown_trans, Aright_trans)

    Amid_tp = calc_prob(Amid_trans, AA_trans, AB_trans, AC_trans, AD_trans, Amid_trans,
                        Aleft_trans, Aup_trans, Adown_trans, Aright_trans)

    Aleft_tp = calc_prob(Aleft_trans, AA_trans, AB_trans, AC_trans, AD_trans, Amid_trans,
                         Aleft_trans, Aup_trans, Adown_trans, Aright_trans)

    Aup_tp = calc_prob(Aup_trans, AA_trans, AB_trans, AC_trans, AD_trans, Amid_trans,
                       Aleft_trans, Aup_trans, Adown_trans, Aright_trans)

    Adown_tp = calc_prob(Adown_trans, AA_trans, AB_trans, AC_trans, AD_trans, Amid_trans,
                         Aleft_trans, Aup_trans, Adown_trans, Aright_trans)

    Aright_tp = calc_prob(Aright_trans, AA_trans, AB_trans, AC_trans, AD_trans, Amid_trans,
                          Aleft_trans, Aup_trans, Adown_trans, Aright_trans)

    BA_tp = calc_prob(BA_trans, BA_trans, BB_trans, BC_trans, BD_trans, Bmid_trans,
                      Bleft_trans, Bup_trans, Bdown_trans, Bright_trans)

    BB_tp = calc_prob(BB_trans, BA_trans, BB_trans, BC_trans, BD_trans, Bmid_trans,
                      Bleft_trans, Bup_trans, Bdown_trans, Bright_trans)

    BC_tp = calc_prob(BC_trans, BA_trans, BB_trans, BC_trans, BD_trans, Bmid_trans,
                      Bleft_trans, Bup_trans, Bdown_trans, Bright_trans)

    BD_tp = calc_prob(BD_trans, BA_trans, BB_trans, BC_trans, BD_trans, Bmid_trans,
                      Bleft_trans, Bup_trans, Bdown_trans, Bright_trans)

    Bmid_tp = calc_prob(Bmid_trans, BA_trans, BB_trans, BC_trans, BD_trans, Bmid_trans,
                        Bleft_trans, Bup_trans, Bdown_trans, Bright_trans)

    Bup_tp = calc_prob(Bup_trans, BA_trans, BB_trans, BC_trans, BD_trans, Bmid_trans,
                       Bleft_trans, Bup_trans, Bdown_trans, Bright_trans)

    Bdown_tp = calc_prob(Bdown_trans, BA_trans, BB_trans, BC_trans, BD_trans, Bmid_trans,
                         Bleft_trans, Bup_trans, Bdown_trans, Bright_trans)

    Bleft_tp = calc_prob(Bleft_trans, BA_trans, BB_trans, BC_trans, BD_trans, Bmid_trans,
                         Bleft_trans, Bup_trans, Bdown_trans, Bright_trans)

    Bright_tp = calc_prob(Bright_trans, BA_trans, BB_trans, BC_trans, BD_trans, Bmid_trans,
                          Bleft_trans, Bup_trans, Bdown_trans, Bright_trans)

    CA_tp = calc_prob(CA_trans, CA_trans, CB_trans, CC_trans, CD_trans, Cmid_trans,
                      Cleft_trans, Cup_trans, Cdown_trans, Cright_trans)

    CB_tp = calc_prob(CB_trans, CA_trans, CB_trans, CC_trans, CD_trans, Cmid_trans,
                      Cleft_trans, Cup_trans, Cdown_trans, Cright_trans)

    CC_tp = calc_prob(CC_trans, CA_trans, CB_trans, CC_trans, CD_trans, Cmid_trans,
                      Cleft_trans, Cup_trans, Cdown_trans, Cright_trans)

    CD_tp = calc_prob(CD_trans, CA_trans, CB_trans, CC_trans, CD_trans, Cmid_trans,
                      Cleft_trans, Cup_trans, Cdown_trans, Cright_trans)

    Cmid_tp = calc_prob(Cmid_trans, CA_trans, CB_trans, CC_trans, CD_trans, Cmid_trans,
                        Cleft_trans, Cup_trans, Cdown_trans, Cright_trans)

    Cup_tp = calc_prob(Cup_trans, CA_trans, CB_trans, CC_trans, CD_trans, Cmid_trans,
                       Cleft_trans, Cup_trans, Cdown_trans, Cright_trans)

    Cdown_tp = calc_prob(Cdown_trans, CA_trans, CB_trans, CC_trans, CD_trans, Cmid_trans,
                         Cleft_trans, Cup_trans, Cdown_trans, Cright_trans)

    Cleft_tp = calc_prob(Cleft_trans, CA_trans, CB_trans, CC_trans, CD_trans, Cmid_trans,
                         Cleft_trans, Cup_trans, Cdown_trans, Cright_trans)

    Cright_tp = calc_prob(Cright_trans, CA_trans, CB_trans, CC_trans, CD_trans, Cmid_trans,
                          Cleft_trans, Cup_trans, Cdown_trans, Cright_trans)

    DA_tp = calc_prob(DA_trans, DA_trans, DB_trans, DC_trans, DD_trans, Dmid_trans,
                      Dleft_trans, Dup_trans, Ddown_trans, Dright_trans)

    DB_tp = calc_prob(DB_trans, DB_trans, DB_trans, DC_trans, DD_trans, Dmid_trans,
                      Dleft_trans, Dup_trans, Ddown_trans, Dright_trans)

    DC_tp = calc_prob(DC_trans, DC_trans, DB_trans, DC_trans, DD_trans, Dmid_trans,
                      Dleft_trans, Dup_trans, Ddown_trans, Dright_trans)

    DD_tp = calc_prob(DD_trans, DD_trans, DB_trans, DC_trans, DD_trans, Dmid_trans,
                      Dleft_trans, Dup_trans, Ddown_trans, Dright_trans)

    Dmid_tp = calc_prob(Dmid_trans, DA_trans, DB_trans, DC_trans, DD_trans, Dmid_trans,
                        Dleft_trans, Dup_trans, Ddown_trans, Dright_trans)

    Dup_tp = calc_prob(Dup_trans, DA_trans, DB_trans, DC_trans, DD_trans, Dmid_trans,
                       Dleft_trans, Dup_trans, Ddown_trans, Dright_trans)

    Ddown_tp = calc_prob(Ddown_trans, DA_trans, DB_trans, DC_trans, DD_trans, Dmid_trans,
                         Dleft_trans, Dup_trans, Ddown_trans, Dright_trans)

    Dleft_tp = calc_prob(Dleft_trans, DA_trans, DB_trans, DC_trans, DD_trans, Dmid_trans,
                         Dleft_trans, Dup_trans, Ddown_trans, Dright_trans)

    Dright_tp = calc_prob(Dright_trans, DA_trans, DB_trans, DC_trans, DD_trans, Dmid_trans,
                          Dleft_trans, Dup_trans, Ddown_trans, Dright_trans)

    info_return = {'test_moves': moves_per_test, 'games_test': game_num_test,
                   'scen_test': scenario_per_test, 'test_dist': test_dist_list, 'AAtrans': AA_trans, 'ABtrans': AB_trans, 'ACtrans': AC_trans, 'ADtrans': AD_trans,
                      'Amidtrans': Amid_trans, 'Alefttrans': Aleft_trans, 'Arighttrans': Aright_trans,
                      'Auptrans': Aup_trans, 'Adowntrans': Adown_trans, 'AAtp': AA_tp, 'ABtp': AB_tp, 'ACtp': AC_tp,
                      'ADtp': AD_tp, 'Amidtp': Amid_tp,
                      'Auptp': Aup_tp, 'Adowntp': Adown_tp,
                      'Alefttp': Aleft_tp, 'Arighttp': Aright_tp,
                      'BAtrans': BA_trans, 'BBtrans': BB_trans, 'BCtrans': BC_trans, 'BDtrans': BD_trans,
                      'Bmidtrans': Bmid_trans, 'Blefttrans': Bleft_trans, 'Brighttrans': Bright_trans,
                      'Buptrans': Bup_trans, 'Bdowntrans': Bdown_trans, 'BAtp': BA_tp, 'BBtp': BB_tp, 'BCtp': BC_tp,
                      'BDtp': BD_tp, 'Bmidtp': Bmid_tp,
                      'Buptp': Bup_tp, 'Bdowntp': Bdown_tp,
                      'Blefttp': Bleft_tp, 'Brighttp': Bright_tp,
                      'CAtrans': CA_trans, 'CBtrans': CB_trans, 'CCtrans': CC_trans, 'CDtrans': CD_trans,
                      'Cmidtrans': Cmid_trans, 'Clefttrans': Cleft_trans, 'Crighttrans': Cright_trans,
                      'Cuptrans': Cup_trans, 'Cdowntrans': Cdown_trans, 'CAtp': CA_tp, 'CBtp': CB_tp, 'CCtp': CC_tp,
                      'CDtp': CD_tp, 'Cmidtp': Cmid_tp,
                      'Cuptp': Cup_tp, 'Cdowntp': Cdown_tp,
                      'Clefttp': Cleft_tp, 'Crighttp': Cright_tp,
                      'DAtrans': DA_trans, 'DBtrans': DB_trans, 'DCtrans': DC_trans, 'DDtrans': DD_trans,
                      'Dmidtrans': Dmid_trans, 'Dlefttrans': Dleft_trans, 'Drighttrans': Dright_trans,
                      'Duptrans': Dup_trans, 'Ddowntrans': Ddown_trans, 'DAtp': DD_tp, 'DBtp': DB_tp, 'DCtp': DC_tp,
                      'DDtp': DD_tp, 'Dmidtp': Dmid_tp,
                      'Duptp': Dup_tp, 'Ddowntp': Ddown_tp,
                      'Dlefttp': Dleft_tp, 'Drighttp': Dright_tp}
    print("Model {} test: complete".format(model))

    return info_return
