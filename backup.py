import numpy as np
import random
import collections.abc


def qtables_8(train_pattern, test_pattern, train_iterations, test_iterations):
    base_reward = 20
    act_step_cost = 1
    exp_rate = 0.2
    alpha = 0.2  # learning rate
    gamma = 0.8  # discount factor # todo: incorporate

    train_seq = train_pattern * train_iterations
    games = len(train_seq)
    game = 0
    moves_per_train = []
    game_num_train = []
    scenario_per_train = []
    moves_per_test = []
    game_num_test = []
    scenario_per_test = []

    into_int_state = False
    test_state = False
    int_move_counter = 4
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
    rewards_A = {}
    rewards_B = {}
    rewards_C = {}
    rewards_D = {}
    rewards_A_int = {}
    rewards_B_int = {}
    rewards_C_int = {}
    rewards_D_int = {}
    rewards_A_count = {}
    rewards_B_count = {}
    rewards_C_count = {}
    rewards_D_count = {}
    rewards_A_intcount = {}
    rewards_B_intcount = {}
    rewards_C_intcount = {}
    rewards_D_intcount = {}
    rewards_A_testcount = {}
    rewards_B_testcount = {}
    rewards_C_testcount = {}
    rewards_D_testcount = {}
    rewards_A_inttestcount = {}
    rewards_B_inttestcount = {}
    rewards_C_inttestcount = {}
    rewards_D_inttestcount = {}
    blank = {}
    for i in range(board_rows):
        for j in range(board_cols):
            rewards_A[(i, j)] = 0
            rewards_B[(i, j)] = 0
            rewards_C[(i, j)] = 0
            rewards_D[(i, j)] = 0
            rewards_A_int[(i, j)] = 0
            rewards_B_int[(i, j)] = 0
            rewards_C_int[(i, j)] = 0
            rewards_D_int[(i, j)] = 0
            rewards_A_count[(i, j)] = 0
            rewards_B_count[(i, j)] = 0
            rewards_C_count[(i, j)] = 0
            rewards_D_count[(i, j)] = 0
            rewards_A_intcount[(i, j)] = 0
            rewards_B_intcount[(i, j)] = 0
            rewards_C_intcount[(i, j)] = 0
            rewards_D_intcount[(i, j)] = 0
            rewards_A_testcount[(i, j)] = 0
            rewards_B_testcount[(i, j)] = 0
            rewards_C_testcount[(i, j)] = 0
            rewards_D_testcount[(i, j)] = 0
            rewards_A_inttestcount[(i, j)] = 0
            rewards_B_inttestcount[(i, j)] = 0
            rewards_C_inttestcount[(i, j)] = 0
            rewards_D_inttestcount[(i, j)] = 0
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
        rewards_A_int[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                            (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_B_int[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                            (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_C_int[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                            (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_D_int[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                            (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_A_count[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                              (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_B_count[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                              (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_C_count[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                              (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_D_count[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                              (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_A_intcount[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                                 (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_B_intcount[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                                 (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_C_intcount[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                                 (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_D_intcount[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                                 (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_A_testcount[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                                  (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_B_testcount[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                                  (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_C_testcount[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                                  (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_D_testcount[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                                  (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_A_inttestcount[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                                     (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_B_inttestcount[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                                     (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_C_inttestcount[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                                     (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        rewards_D_inttestcount[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                                     (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}
        blank[i] = {(-1, 0): 0, (1, 0): 0, (0, -1): 0, (0, 1): 0,
                    (-1, -1): 0, (-1, 1): 0, (1, -1): 0, (1, 1): 0, (0, 0): 0}

    A_int_offlimits = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 0), (4, 1), (4, 2), (4, 3)]
    B_int_offlimits = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    C_int_offlimits = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 0), (4, 1), (4, 2), (4, 3)]
    D_int_offlimits = [(1, 0), (2, 0), (3, 0), (4, 0), (4, 4), (0, 0), (0, 1), (0, 2), (0, 3)]
    for a in A_int_offlimits:
        for i in range(-1, 2):
            for j in range(-1, 2):
                rewards_A_int[a][(i, j)] = 5.6789
    for a in B_int_offlimits:
        for i in range(-1, 2):
            for j in range(-1, 2):
                rewards_B_int[a][(i, j)] = 5.6789
    for a in C_int_offlimits:
        for i in range(-1, 2):
            for j in range(-1, 2):
                rewards_C_int[a][(i, j)] = 5.6789
    for a in D_int_offlimits:
        for i in range(-1, 2):
            for j in range(-1, 2):
                rewards_D_int[a][(i, j)] = 5.6789

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
                        poss_reward = rewards_A[current_pos][act_action_trans[a]]
                        if poss_reward > best_reward:
                            next_act_action = a
                            best_reward = poss_reward
                    elif win_target == "B":
                        poss_reward = rewards_B[current_pos][act_action_trans[a]]
                        if poss_reward > best_reward:
                            next_act_action = a
                            best_reward = poss_reward
                    elif win_target == "C":
                        poss_reward = rewards_C[current_pos][act_action_trans[a]]
                        if poss_reward > best_reward:
                            next_act_action = a
                            best_reward = poss_reward
                    else:
                        poss_reward = rewards_D[current_pos][act_action_trans[a]]
                        if poss_reward > best_reward:
                            next_act_action = a
                            best_reward = poss_reward
            new_position = take_next_move(next_act_action)
            if new_position == current_pos and next_act_action != "stay":
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
                        poss_reward = rewards_A_int[current_pos][int_action_trans[a]]
                        if poss_reward > best_reward:
                            next_int_action = a
                            best_reward = poss_reward
                    elif prev_target == "B":
                        poss_reward = rewards_B_int[current_pos][int_action_trans[a]]
                        if poss_reward > best_reward:
                            next_int_action = a
                            best_reward = poss_reward
                    elif prev_target == "C":
                        poss_reward = rewards_C_int[current_pos][int_action_trans[a]]
                        if poss_reward > best_reward:
                            next_int_action = a
                            best_reward = poss_reward
                    else:
                        poss_reward = rewards_D_int[current_pos][int_action_trans[a]]
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

    def update_int_rewards(reward_apply):
        if game == 0:
            return
        reversed_int_list = unique(list(reversed(int_action_list)))
        for a, b in reversed_int_list:
            if prev_scenario == "A":
                rewards_A_int[a][b] = round(
                    rewards_A_int[a][b] + alpha * (reward_apply - rewards_A_int[a][b]), 2)
            elif prev_scenario == "B":
                rewards_B_int[a][b] = round(
                    rewards_B_int[a][b] + alpha * (reward_apply - rewards_B_int[a][b]), 2)
            elif prev_scenario == "C":
                rewards_C_int[a][b] = round(
                    rewards_C_int[a][b] + alpha * (reward_apply - rewards_C_int[a][b]), 2)
            else:
                rewards_D_int[a][b] = round(
                    rewards_D_int[a][b] + alpha * (reward_apply - rewards_D_int[a][b]), 2)


    def int_action_count(currpos, move, prevscenario):
        if not test_state:
            if prevscenario == "A":
                rewards_A_intcount[currpos][move] += 1
            if prevscenario == "B":
                rewards_B_intcount[currpos][move] += 1
            if prevscenario == "C":
                rewards_C_intcount[currpos][move] += 1
            if prevscenario == "D":
                rewards_D_intcount[currpos][move] += 1
        else:
            if prevscenario == "A":
                rewards_A_inttestcount[currpos][move] += 1
            if prevscenario == "B":
                rewards_B_inttestcount[currpos][move] += 1
            if prevscenario == "C":
                rewards_C_inttestcount[currpos][move] += 1
            if prevscenario == "D":
                rewards_D_inttestcount[currpos][move] += 1

    def act_action_count(currpos, move, scenario):
        if not test_state:
            if scenario == "A":
                rewards_A_count[currpos][move] += 1
            if scenario == "B":
                rewards_B_count[currpos][move] += 1
            if scenario == "C":
                rewards_C_count[currpos][move] += 1
            if scenario == "D":
                rewards_D_count[currpos][move] += 1
        else:
            if scenario == "A":
                rewards_A_testcount[currpos][move] += 1
            if scenario == "B":
                rewards_B_testcount[currpos][move] += 1
            if scenario == "C":
                rewards_C_testcount[currpos][move] += 1
            if scenario == "D":
                rewards_D_testcount[currpos][move] += 1

    def check_to_int():
        if int_move_counter < 4 and into_int_state:
            return True
        return False

    def unique(sequence):
        seen = set()
        return [x for x in sequence if not (x in seen or seen.add(x))]

    while game < games:
        scenario = train_seq[game]
        win_pos = set_win_pos(scenario)
        go_to_int = check_to_int()
        if go_to_int:
            int_action = pick_int_move(prev_scenario)
            int_action_coord = int_action_trans[int_action]
            int_action_list.append((current_pos, int_action_coord))
            int_action_count(current_pos, int_action_coord, prev_scenario)
            current_pos = take_next_move(int_action)
            int_move_counter += 1
        else:
            into_int_state = False
            int_move_counter = 0
            if current_pos == win_pos:
                reward = base_reward - (act_move_counter * act_step_cost)
                update_act_rewards(reward)
                update_int_rewards(reward)
                if (game + 1) % (games / 10) == 0:
                    print("Model 1 training game {} of {} completed:  Act moves in last game: {}".format(
                        game + 1,
                        games,
                        act_move_counter))
                moves_per_train.append(act_move_counter)
                game_num_train.append(game + 1)
                scenario_per_train.append(scenario)
                game += 1
                act_move_counter = 0
                int_action_list = []
                act_action_list = []
                into_int_state = True
                prev_scenario = scenario
            else:  # take another move in action state
                act_action = pick_act_move(scenario)
                act_action_coord = act_action_trans[act_action]
                act_action_list.append((current_pos, act_action_coord))
                act_action_count(current_pos, act_action_coord, scenario)
                current_pos = take_next_move(act_action)
                act_move_counter += 1

    test_seq = test_pattern * test_iterations
    games = len(test_seq)
    game = 0
    current_pos = (2, 2)
    into_int_state = False

    while game < games:
        scenario = test_seq[game]
        win_pos = set_win_pos(scenario)
        go_to_int = check_to_int()
        if go_to_int:
            int_action = pick_int_move(prev_scenario)
            int_action_coord = int_action_trans[int_action]
            int_action_list.append((current_pos, int_action_coord))
            int_action_count(current_pos, int_action_coord, prev_scenario)
            current_pos = take_next_move(int_action)
            int_move_counter += 1
        else:
            into_int_state = False
            int_move_counter = 0
            if current_pos == win_pos:
                if (game + 1) % (games / 10) == 0:
                    print("Model 1 testing game {} of {} completed:  Act moves in last game: {}".format(
                        game + 1,
                        games,
                        act_move_counter))
                moves_per_test.append(act_move_counter)
                game_num_test.append(game + 1)
                scenario_per_test.append(scenario)
                game += 1
                act_move_counter = 0
                int_action_list = []
                act_action_list = []
                into_int_state = True
                prev_scenario = scenario
            else:  # take another move in action state
                act_action = pick_act_move(scenario)
                act_action_coord = act_action_trans[act_action]
                act_action_list.append((current_pos, act_action_coord))
                act_action_count(current_pos, act_action_coord, scenario)
                current_pos = take_next_move(act_action)
                act_move_counter += 1
    return {'A': rewards_A, 'B': rewards_B, 'C': rewards_C, 'D': rewards_D, 'Aint': rewards_A_int,
            'Bint': rewards_B_int, 'Cint': rewards_C_int,
            'Dint': rewards_D_int, 'train_moves': moves_per_train, 'games_train': game_num_train,
            'scen_train': scenario_per_train, 'test_moves': moves_per_test, 'games_test': game_num_test,
            'scen_test': scenario_per_test, "Acount": rewards_A_count, "Bcount": rewards_B_count,
            "Ccount": rewards_C_count, "Dcount": rewards_D_count, "Aintcount": rewards_A_intcount,
            "Bintcount": rewards_B_intcount, "Cintcount": rewards_C_intcount, "Dintcount": rewards_D_intcount,
            "Atestcount": rewards_A_testcount, "Btestcount": rewards_B_testcount,
            "Ctestcount": rewards_C_testcount, "Dtestcount": rewards_D_testcount,
            "Atestintcount": rewards_A_inttestcount, "Btestintcount": rewards_B_inttestcount,
            "Ctestintcount": rewards_C_inttestcount, "Dtestintcount": rewards_D_inttestcount}