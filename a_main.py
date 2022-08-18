import b_modelselector
import z_statistics
import a_tester
from z_visualization import visualize_tables
from collections import defaultdict


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Sequences:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

seq1 = 'DBCBABABDACBADACACBDACACADBDCDBDACADBCBDADBCDCBC'  # G = .25
seq2 = 'ABCACABABACDCDABDBDBDCABDCDBDCDCABCDBACDBACACDBA'  # G = .40
seq3 = 'BADCDCBDABCBABADCDCBCBCBACBADADADCDABADADCBCBCDA'  # G = .44
seq4 = 'DBCDBACACACACDBDBDBACACACDBCDBACACDABABDBDBACDBD'  # G = .55
seq5 = 'DCDCDCBADCBADCBADCBADCBACBADCBACBABADCBABADCDBAD'  # G = .68
seq6 = 'CBCBDACBDADACBCBCBDACBDACBCBDACBDADACBDADADADACB'  # G = .76
seq7 = 'BCADADADBCADBCADBCADBCADBCBCBCBCADADBCADBCADBCAD'  # G = .79
seq8 = 'BCDABCDABCBCDABCDABCDABCDABCDADABCDABCDABCDABCDA'  # G = .89
seq9 = 'BACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACDBACD'  # G = 1.0
seq10 = 'ABDCABDCABDCABDCABDCABDCABDCABDCABDCABDCABDCABDC'  # G = 1.0
seq11 = 'DCBADCBADCBADCBADCBADCBADCBADCBADCBADCBADCBADCBA'  # G = 1.0

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Models:
1: action-distribution, positive rewards
2: epsilon-greedy, positive rewards
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Select training criteria, models, and desired reports
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

train_pattern = seq3
train_iterations = 100
train_sets = 20

model_list = [1, 2]

statistics = True
visualizations = True

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Run program
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


summaryinfo = {}
test_pattern = train_pattern
test_iterations = 1

for a in model_list:
    summaryinfo[a] = {}
    summaryinfo[a]['trainiter'] = train_iterations
    summaryinfo[a]['trainsets'] = train_sets
    if test_pattern == seq1:
        summaryinfo[a]['sequence'] = 'Seq1'
    if test_pattern == seq2:
        summaryinfo[a]['sequence'] = 'Seq2'
    if test_pattern == seq3:
        summaryinfo[a]['sequence'] = 'Seq3'
    if test_pattern == seq4:
        summaryinfo[a]['sequence'] = 'Seq4'
    if test_pattern == seq5:
        summaryinfo[a]['sequence'] = 'Seq5'
    if test_pattern == seq6:
        summaryinfo[a]['sequence'] = 'Seq6'
    if test_pattern == seq7:
        summaryinfo[a]['sequence'] = 'Seq7'
    if test_pattern == seq8:
        summaryinfo[a]['sequence'] = 'Seq8'
    if test_pattern == seq9:
        summaryinfo[a]['sequence'] = 'Seq9'
    if test_pattern == seq10:
        summaryinfo[a]['sequence'] = 'Seq10'
    if test_pattern == seq11:
        summaryinfo[a]['sequence'] = 'Seq11'

    if a == 1:
        summaryinfo[1]['description'] = '1: action-distribution, positive rewards'
    if a == 2:
        summaryinfo[2]['description'] = '2: epsilon-greedy, positive rewards'


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
    if statistics:
        z_statistics.stats(model, test_results, test_sequence, summaryinfo[model])
    if visualizations:
        visualize_tables(model, resultsfinal[model])


"""""""""
Statistics/visualization to add:
- making a summary excel to compare models
other stats:
- variance of Q values across sets
- % of time int state leads directly to target
"""""""""
