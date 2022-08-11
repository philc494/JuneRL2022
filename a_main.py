import b_modelselector
import z_statistics
from z_visualization import visualize_tables
import pandas as pd
from collections import defaultdict


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
I. Select parameters
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
train_pattern = "AB"
test_pattern = train_pattern
train_iterations = 250
train_sets = 20
test_iterations = 1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
II. Select models to analyze:
0: Orig backup
1: 8 Q-tables: negative reward possible
2: 8 Q-tablespos: game over at 50, no negative rewards
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
model_list = [2]


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
III. Run program
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

parameters = {'train_pattern': train_pattern, 'test_pattern': test_pattern, 'train_iterations': train_iterations,
              'test_iterations': test_iterations}

(input(" ---Train/Test Settings--- \n "
              "Training pattern: {}\n Iterations: {}\n Total training games: {}\n Testing pattern: {}\n Testing iterations: {}\n"
                " Total testing games: {}\n  "
              "---Press enter to continue--- ".format(train_pattern, train_iterations, len(train_pattern) * train_iterations,
                                                           test_pattern, test_iterations, len(test_pattern) * test_iterations,
                                                           )))
results = {}
reward_results = {}
stats = {}
train_sets_done = 0


""" Generate multiple sets of training data for averaging"""
for model in model_list:
    reward_results[model] = {}
    for x in range(0, train_sets):
        reward_results[model][x] = b_modelselector.model_selector(model, parameters)[0]
        print("Model {}, set {} completed".format(model, train_sets_done + 1))
        train_sets_done += 1


"""Calculate average and populate a final results dictionary"""
set_list = []
table_list = []
pos_list = []
act_list = []
resultsfinal = defaultdict(dict)
reward_tempdic = defaultdict(dict)

for a in reward_results[2]:
    set_list.append(a)
for a in reward_results[2][0]:
    table_list.append(a)
for a in reward_results[2][0]['A']:
    pos_list.append(a)
for a in reward_results[2][0]['A']:
    for b in reward_results[2][0]['A'][a]:
        act_list.append(b)

for a in model_list:
    reward_tempdic[a] = defaultdict(dict)
    resultsfinal[a] = defaultdict(dict)
    for b in table_list:
        reward_tempdic[a][b] = defaultdict(dict)
        resultsfinal[a][b] = defaultdict(dict)
        for c in pos_list:
            reward_tempdic[a][b][c] = defaultdict(dict)
            resultsfinal[a][b][c] = defaultdict(dict)
            for d in act_list:
                reward_tempdic[a][b][c][d] = defaultdict(dict)
                resultsfinal[a][b][c][d] = defaultdict(dict)
                for x in set_list:
                    reward_tempdic[a][b][c][d][x] = reward_results[a][x][b][c][d]

for a in model_list:
    for b in table_list:
        for c in pos_list:
            for d in act_list:
                resultsfinal[a][b][c][d] = round(sum(reward_tempdic[a][b][c][d].values()) / len(set_list), 2)

print(reward_tempdic[2]['A'][(3, 3)])
print(resultsfinal[2]['A'][(3, 3)])

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Run statistics and visualizations based on this final averaged set for each model
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

for model in model_list:
    # stats[resultsfinal[model]] = z_statistics.stats(resultsfinal[model], results)
    visualize_tables(model, resultsfinal[model])




"""""""""
Statistics/visualization to add:
- plotting DFs from different models in same file for comparison
- plotting epochs/etc from different models in same graph for comparison
- plot all the parameters used to avoid confusion of which model was run
other stats:
- time to run
- % of time int state leads directly to target
- test: average moves per game 
- train/test: ratio of avg test game length to avg train game length
- test: average distance after int state to next target
- test: average distance from middle after int state
- test: average times per game wrong corner touched before right corner
- 
"""
