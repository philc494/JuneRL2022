import b_modelselector
import z_statistics
import a_tester
from z_visualization import visualize_tables
from collections import defaultdict


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
I. Select parameters
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
train_pattern = "ABCD"
test_pattern = train_pattern
train_iterations = 100
train_sets = 100

test_iterations = 1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
II. Select models to analyze:
0: Orig backup
1: 8 Q-tables: positive rewards, action-distribution
2: 8 Q-tablespos: positive rewards, epsilon-greedy
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

model_list = [1]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
III. Run program
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

parameters = {'train_pattern': train_pattern, 'test_pattern': test_pattern, 'train_iterations': train_iterations,
              'test_iterations': test_iterations}

(input(" ---Train/Test Settings--- \n "
              "Training pattern: {}\n Iterations: {}\n Training sets: {}\n\n Testing pattern: {}\n"
       " Testing iterations: {}\n  "
              "---Press enter to continue--- ".format(train_pattern, train_iterations,
                                                            train_sets,
                                                           test_pattern, test_iterations, len(test_pattern) * test_iterations,
                                                           )))
results = {}
reward_results = {}
stats = {}
train_sets_done = 0
test_sequence = test_pattern * test_iterations


""" Generate multiple sets of training data for averaging"""
for model in model_list:
    reward_results[model] = {}
    train_sets_done = 0
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

for a in reward_results[model]:
    set_list.append(a)
for a in reward_results[model][0]:
    table_list.append(a)
for a in reward_results[model][0]['A']:
    pos_list.append(a)
for a in reward_results[model][0]['A']:
    for b in reward_results[model][0]['A'][a]:
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


print(reward_tempdic[model]['A'][(1, 0)][(-1, 0)])
print(resultsfinal[model]['A'][(1, 0)][(-1, 0)])

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Run statistics and visualizations based on this final averaged set for each model
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

for model in model_list:
    test_results = a_tester.test_model(resultsfinal[model], test_sequence, model)
    z_statistics.stats(model, test_results)
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
