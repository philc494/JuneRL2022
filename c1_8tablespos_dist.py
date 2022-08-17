import numpy as np
import random
import collections.abc
from math import e


def qtables_8(train_pattern, train_iterations):
    base_reward = 100
    alpha = 0.2

    train_seq = train_pattern * train_iterations
    games = len(train_seq)
    game = 0
    moves_per_train = []
    game_num_train = []
    scenario_per_train = []

    into_int_state = False
    test_state = False
    int_move_counter = 4
    act_move_counter = 0
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

    def get_exp(n):
        return e ** n

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
            act_rewards = []
            next_act_action = ""
            if win_target == "A":
                up_reward = rewards_A[current_pos][act_action_trans['up']]
                down_reward = rewards_A[current_pos][act_action_trans['down']]
                left_reward = rewards_A[current_pos][act_action_trans['left']]
                right_reward = rewards_A[current_pos][act_action_trans['right']]
                uleft_reward = rewards_A[current_pos][act_action_trans['uleft']]
                uright_reward = rewards_A[current_pos][act_action_trans['uright']]
                dleft_reward = rewards_A[current_pos][act_action_trans['dleft']]
                dright_reward = rewards_A[current_pos][act_action_trans['dright']]
                stay_reward = rewards_A[current_pos][act_action_trans['stay']]
                act_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                    uleft_reward, uright_reward, dleft_reward, dright_reward,
                                    stay_reward])
                total_reward = sum(act_rewards)
                if total_reward == 0:
                    next_act_action = random.choice(act_actions)
                else:
                    up_ratio = up_reward / total_reward
                    down_ratio = down_reward / total_reward
                    left_ratio = left_reward / total_reward
                    right_ratio = right_reward / total_reward
                    uleft_ratio = uleft_reward / total_reward
                    uright_ratio = uright_reward / total_reward
                    dleft_ratio = dleft_reward / total_reward
                    dright_ratio = dright_reward / total_reward
                    stay_ratio = stay_reward / total_reward
                    next_act_action = random.choices(act_actions, weights=(up_ratio, down_ratio,
                                left_ratio, right_ratio, uleft_ratio, uright_ratio,
                                dleft_ratio, dright_ratio, stay_ratio), k=1)[0]

            elif win_target == "B":
                up_reward = rewards_B[current_pos][act_action_trans['up']]
                down_reward = rewards_B[current_pos][act_action_trans['down']]
                left_reward = rewards_B[current_pos][act_action_trans['left']]
                right_reward = rewards_B[current_pos][act_action_trans['right']]
                uleft_reward = rewards_B[current_pos][act_action_trans['uleft']]
                uright_reward = rewards_B[current_pos][act_action_trans['uright']]
                dleft_reward = rewards_B[current_pos][act_action_trans['dleft']]
                dright_reward = rewards_B[current_pos][act_action_trans['dright']]
                stay_reward = rewards_B[current_pos][act_action_trans['stay']]
                act_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                    uleft_reward, uright_reward, dleft_reward, dright_reward,
                                    stay_reward])
                total_reward = sum(act_rewards)
                if total_reward == 0:
                    next_act_action = random.choice(act_actions)
                else:
                    up_ratio = up_reward / total_reward
                    down_ratio = down_reward / total_reward
                    left_ratio = left_reward / total_reward
                    right_ratio = right_reward / total_reward
                    uleft_ratio = uleft_reward / total_reward
                    uright_ratio = uright_reward / total_reward
                    dleft_ratio = dleft_reward / total_reward
                    dright_ratio = dright_reward / total_reward
                    stay_ratio = stay_reward / total_reward
                    next_act_action = random.choices(act_actions, weights=(up_ratio, down_ratio,
                                                                           left_ratio, right_ratio, uleft_ratio,
                                                                           uright_ratio,
                                                                           dleft_ratio, dright_ratio, stay_ratio), k=1)[0]
            elif win_target == "C":
                up_reward = rewards_C[current_pos][act_action_trans['up']]
                down_reward = rewards_C[current_pos][act_action_trans['down']]
                left_reward = rewards_C[current_pos][act_action_trans['left']]
                right_reward = rewards_C[current_pos][act_action_trans['right']]
                uleft_reward = rewards_C[current_pos][act_action_trans['uleft']]
                uright_reward = rewards_C[current_pos][act_action_trans['uright']]
                dleft_reward = rewards_C[current_pos][act_action_trans['dleft']]
                dright_reward = rewards_C[current_pos][act_action_trans['dright']]
                stay_reward = rewards_C[current_pos][act_action_trans['stay']]
                act_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                    uleft_reward, uright_reward, dleft_reward, dright_reward,
                                    stay_reward])
                total_reward = sum(act_rewards)
                if total_reward == 0:
                    next_act_action = random.choice(act_actions)
                else:
                    up_ratio = up_reward / total_reward
                    down_ratio = down_reward / total_reward
                    left_ratio = left_reward / total_reward
                    right_ratio = right_reward / total_reward
                    uleft_ratio = uleft_reward / total_reward
                    uright_ratio = uright_reward / total_reward
                    dleft_ratio = dleft_reward / total_reward
                    dright_ratio = dright_reward / total_reward
                    stay_ratio = stay_reward / total_reward
                    next_act_action = random.choices(act_actions, weights=(up_ratio, down_ratio,
                                                                           left_ratio, right_ratio, uleft_ratio,
                                                                           uright_ratio,
                                                                           dleft_ratio, dright_ratio, stay_ratio), k=1)[0]
            else:
                up_reward = rewards_D[current_pos][act_action_trans['up']]
                down_reward = rewards_D[current_pos][act_action_trans['down']]
                left_reward = rewards_D[current_pos][act_action_trans['left']]
                right_reward = rewards_D[current_pos][act_action_trans['right']]
                uleft_reward = rewards_D[current_pos][act_action_trans['uleft']]
                uright_reward = rewards_D[current_pos][act_action_trans['uright']]
                dleft_reward = rewards_D[current_pos][act_action_trans['dleft']]
                dright_reward = rewards_D[current_pos][act_action_trans['dright']]
                stay_reward = rewards_D[current_pos][act_action_trans['stay']]
                act_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                    uleft_reward, uright_reward, dleft_reward, dright_reward,
                                    stay_reward])
                total_reward = sum(act_rewards)
                if total_reward == 0:
                    next_act_action = random.choice(act_actions)
                else:
                    up_ratio = up_reward / total_reward
                    down_ratio = down_reward / total_reward
                    left_ratio = left_reward / total_reward
                    right_ratio = right_reward / total_reward
                    uleft_ratio = uleft_reward / total_reward
                    uright_ratio = uright_reward / total_reward
                    dleft_ratio = dleft_reward / total_reward
                    dright_ratio = dright_reward / total_reward
                    stay_ratio = stay_reward / total_reward
                    next_act_action = random.choices(act_actions, weights=(up_ratio, down_ratio,
                                                                           left_ratio, right_ratio, uleft_ratio,
                                                                           uright_ratio,
                                                                           dleft_ratio, dright_ratio, stay_ratio), k=1)[0]
            new_position = take_next_move(next_act_action)
            if new_position == current_pos and next_act_action != "stay":
                continue
            else:
                return next_act_action

    def pick_int_move(prev_target):
        while True:
            int_rewards = []
            if prev_target == "A":
                up_reward = rewards_A_int[current_pos][act_action_trans['up']]
                down_reward = rewards_A_int[current_pos][act_action_trans['down']]
                left_reward = rewards_A_int[current_pos][act_action_trans['left']]
                right_reward = rewards_A_int[current_pos][act_action_trans['right']]
                uleft_reward = rewards_A_int[current_pos][act_action_trans['uleft']]
                uright_reward = rewards_A_int[current_pos][act_action_trans['uright']]
                dleft_reward = rewards_A_int[current_pos][act_action_trans['dleft']]
                dright_reward = rewards_A_int[current_pos][act_action_trans['dright']]
                stay_reward = rewards_A_int[current_pos][act_action_trans['stay']]
                int_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                       uleft_reward, uright_reward, dleft_reward, dright_reward,
                                       stay_reward])
                total_reward = sum(int_rewards)
                if total_reward == 0:
                    next_int_action = random.choice(act_actions)
                else:
                    up_ratio = up_reward / total_reward
                    down_ratio = down_reward / total_reward
                    left_ratio = left_reward / total_reward
                    right_ratio = right_reward / total_reward
                    uleft_ratio = uleft_reward / total_reward
                    uright_ratio = uright_reward / total_reward
                    dleft_ratio = dleft_reward / total_reward
                    dright_ratio = dright_reward / total_reward
                    stay_ratio = stay_reward / total_reward
                    next_int_action = random.choices(int_actions, weights=(up_ratio, down_ratio,
                                                                           left_ratio, right_ratio, uleft_ratio,
                                                                           uright_ratio,
                                                                           dleft_ratio, dright_ratio, stay_ratio), k=1)[0]
            elif prev_target == "B":
                up_reward = rewards_B_int[current_pos][act_action_trans['up']]
                down_reward = rewards_B_int[current_pos][act_action_trans['down']]
                left_reward = rewards_B_int[current_pos][act_action_trans['left']]
                right_reward = rewards_B_int[current_pos][act_action_trans['right']]
                uleft_reward = rewards_B_int[current_pos][act_action_trans['uleft']]
                uright_reward = rewards_B_int[current_pos][act_action_trans['uright']]
                dleft_reward = rewards_B_int[current_pos][act_action_trans['dleft']]
                dright_reward = rewards_B_int[current_pos][act_action_trans['dright']]
                stay_reward = rewards_B_int[current_pos][act_action_trans['stay']]
                int_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                    uleft_reward, uright_reward, dleft_reward, dright_reward,
                                    stay_reward])
                total_reward = sum(int_rewards)
                if total_reward == 0:
                    next_int_action = random.choice(act_actions)
                else:
                    up_ratio = up_reward / total_reward
                    down_ratio = down_reward / total_reward
                    left_ratio = left_reward / total_reward
                    right_ratio = right_reward / total_reward
                    uleft_ratio = uleft_reward / total_reward
                    uright_ratio = uright_reward / total_reward
                    dleft_ratio = dleft_reward / total_reward
                    dright_ratio = dright_reward / total_reward
                    stay_ratio = stay_reward / total_reward
                    next_int_action = random.choices(int_actions, weights=(up_ratio, down_ratio,
                                                                           left_ratio, right_ratio, uleft_ratio,
                                                                           uright_ratio,
                                                                           dleft_ratio, dright_ratio, stay_ratio), k=1)[0]
            elif prev_target == "C":
                up_reward = rewards_C_int[current_pos][act_action_trans['up']]
                down_reward = rewards_C_int[current_pos][act_action_trans['down']]
                left_reward = rewards_C_int[current_pos][act_action_trans['left']]
                right_reward = rewards_C_int[current_pos][act_action_trans['right']]
                uleft_reward = rewards_C_int[current_pos][act_action_trans['uleft']]
                uright_reward = rewards_C_int[current_pos][act_action_trans['uright']]
                dleft_reward = rewards_C_int[current_pos][act_action_trans['dleft']]
                dright_reward = rewards_C_int[current_pos][act_action_trans['dright']]
                stay_reward = rewards_C_int[current_pos][act_action_trans['stay']]
                int_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                    uleft_reward, uright_reward, dleft_reward, dright_reward,
                                    stay_reward])
                total_reward = sum(int_rewards)
                if total_reward == 0:
                    next_int_action = random.choice(act_actions)
                else:
                    up_ratio = up_reward / total_reward
                    down_ratio = down_reward / total_reward
                    left_ratio = left_reward / total_reward
                    right_ratio = right_reward / total_reward
                    uleft_ratio = uleft_reward / total_reward
                    uright_ratio = uright_reward / total_reward
                    dleft_ratio = dleft_reward / total_reward
                    dright_ratio = dright_reward / total_reward
                    stay_ratio = stay_reward / total_reward
                    next_int_action = random.choices(int_actions, weights=(up_ratio, down_ratio,
                                                                           left_ratio, right_ratio, uleft_ratio,
                                                                           uright_ratio,
                                                                           dleft_ratio, dright_ratio, stay_ratio), k=1)[0]
            else:
                up_reward = rewards_D_int[current_pos][act_action_trans['up']]
                down_reward = rewards_D_int[current_pos][act_action_trans['down']]
                left_reward = rewards_D_int[current_pos][act_action_trans['left']]
                right_reward = rewards_D_int[current_pos][act_action_trans['right']]
                uleft_reward = rewards_D_int[current_pos][act_action_trans['uleft']]
                uright_reward = rewards_D_int[current_pos][act_action_trans['uright']]
                dleft_reward = rewards_D_int[current_pos][act_action_trans['dleft']]
                dright_reward = rewards_D_int[current_pos][act_action_trans['dright']]
                stay_reward = rewards_D_int[current_pos][act_action_trans['stay']]
                int_rewards.extend([up_reward, down_reward, left_reward, right_reward,
                                    uleft_reward, uright_reward, dleft_reward, dright_reward,
                                    stay_reward])
                total_reward = sum(int_rewards)
                if total_reward == 0:
                    next_int_action = random.choice(act_actions)
                else:
                    up_ratio = up_reward / total_reward
                    down_ratio = down_reward / total_reward
                    left_ratio = left_reward / total_reward
                    right_ratio = right_reward / total_reward
                    uleft_ratio = uleft_reward / total_reward
                    uright_ratio = uright_reward / total_reward
                    dleft_ratio = dleft_reward / total_reward
                    dright_ratio = dright_reward / total_reward
                    stay_ratio = stay_reward / total_reward
                    next_int_action = random.choices(int_actions, weights=(up_ratio, down_ratio,
                                                                           left_ratio, right_ratio, uleft_ratio,
                                                                           uright_ratio,
                                                                           dleft_ratio, dright_ratio, stay_ratio), k=1)[0]
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
            if current_pos == win_pos:
                reward = base_reward * (get_exp(-.25 * act_move_counter))
                update_act_rewards(reward)
                update_int_rewards(reward)
                # if (game + 1) % (games / 2) == 0:
                    # print("Model 2 training game {} of {} completed:  Act moves in last game: {}".format(
                    #     game + 1,
                    #     games,
                    #     act_move_counter))
                moves_per_train.append(act_move_counter)
                game_num_train.append(game + 1)
                scenario_per_train.append(scenario)
                game += 1
                act_move_counter = 0
                int_move_counter = 0
                int_action_list = []
                act_action_list = []
                into_int_state = True
                prev_scenario = scenario
            else:
                act_action = pick_act_move(scenario)
                act_action_coord = act_action_trans[act_action]
                act_action_list.append((current_pos, act_action_coord))
                act_action_count(current_pos, act_action_coord, scenario)
                current_pos = take_next_move(act_action)
                act_move_counter += 1

    rewards_return = {'A': rewards_A, 'B': rewards_B, 'C': rewards_C, 'D': rewards_D, 'Aint': rewards_A_int,
            'Bint': rewards_B_int, 'Cint': rewards_C_int,
            'Dint': rewards_D_int}
    info_return = {'train_moves': moves_per_train, 'games_train': game_num_train,
            'scen_train': scenario_per_train}

    return rewards_return, info_return, {'A': rewards_A, 'B': rewards_B, 'C': rewards_C, 'D': rewards_D, 'Aint': rewards_A_int,
            'Bint': rewards_B_int, 'Cint': rewards_C_int,
            'Dint': rewards_D_int, 'train_moves': moves_per_train, 'games_train': game_num_train,
            'scen_train': scenario_per_train}
