import pandas as pd
import numpy as np
import os


def stats(model, infodic, patttext, testpatt, summary, label, alpha, exploration_rate, exp_val, test_iterations,
          train_iterations, train_sets):
    test_moves = np.array(infodic['test_moves'])
    test_dist = np.array(infodic['test_dist'])
    df_test = pd.DataFrame(
        {'Moves': test_moves, 'Distance': test_dist})
    df_test['Avg Moves'] = df_test['Moves'].mean()
    df_test['Avg Dist'] = df_test['Distance'].mean()
    avg_moves = df_test.at[4, 'Avg Moves']
    avg_dist = df_test.at[4, 'Avg Dist']
    df_result = pd.DataFrame({'Model': [model], 'Label': label, 'Sequence': patttext, 'Pattern': testpatt,
                              'Test Iter': test_iterations, 'Train Iter': train_iterations,
                              'Train Sets': train_sets,
                              'Alpha': alpha, 'Exp Rate': [exploration_rate],
                              'Rew Decay': [exp_val], 'Avg Moves': avg_moves, 'Avg Dist': avg_dist},
                             index=['Summary'])

    directory = str(model)
    parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results/test'
    path = os.path.join(parent_dir, directory)
    writer = pd.ExcelWriter(path + '/' + str(model) + '_' + label + '_test_stats.xlsx', engine='xlsxwriter')
    df_result.to_excel(writer, sheet_name='summary_test')
    writer.save()
    print("Model {} statistics: complete".format(model))

    # test_label = []
    # test_seq = []
    # test_desc = []
    # train_iter = []
    # train_sets = []
    # seq_label = []
    # for a in infodic['test_moves']:
    #     b = 'test'
    #     c = testseq
    #     d = summary['description']
    #     e = summary['trainiter']
    #     f = summary['trainsets']
    #     g = summary['sequence']
    #     test_label.append(b)
    #     test_seq.append(c)
    #     test_desc.append(d)
    #     train_iter.append(e)
    #     train_sets.append(f)
    #     seq_label.append(g)
    #
    # test_moves = np.array(infodic['test_moves'])
    # test_gamenum = np.array(infodic['games_test'])
    # test_gamescen = np.array(infodic['scen_test'])
    # test_dist = np.array(infodic['test_dist'])
    # description = np.array(test_desc)
    # test_pattern = np.array(test_seq)
    # sequence = np.array(seq_label)
    # df_test = pd.DataFrame(
    #     {'Game_num': test_gamenum, 'Scenario': test_gamescen, 'Model': description, 'Seq #': sequence,
    #      'Pattern': test_pattern, 'TrainIter': train_iter,
    #      'TrainSets': train_sets, 'Moves': test_moves, 'Distance': test_dist})
    # df_test['Avg Moves'] = df_test['Moves'].mean()
    #
    # df_test['Avg Dist'] = df_test['Distance'].mean()
    # print("hello")
    # # directory = str(model)
    # # parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results/test'
    # # path = os.path.join(parent_dir, directory)
    # # writer = pd.ExcelWriter(path + '/' + label + '_' + str(model) + '_test_stats.xlsx', engine='xlsxwriter')
    # # df_test.to_excel(writer, sheet_name='summary_test')
    # # df_test.to_csv('test.csv')
    # # writer.save()






