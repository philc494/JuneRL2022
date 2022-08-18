import pandas as pd
import numpy as np
import os


def stats(model, infodic, testseq, summary):
    # train_label = []
    # for a in resultsdic[model]['train_moves']:
    #     b = 'train'
    #     train_label.append(b)
    # train_name = np.array(train_label)
    # train_moves = np.array(resultsdic[model]['train_moves'])
    # train_gamenum = np.array(resultsdic[model]['games_train'])
    # train_gamescen = np.array(resultsdic[model]['scen_train'])
    # df_train = pd.DataFrame({'Game_num': train_gamenum, 'Moves': train_moves, 'Scenario': train_gamescen, 'Type': train_name})
    # df_train['MA100'] = df_train['Moves'].rolling(100).mean()
    #
    # directory = str(model)
    # parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results'
    # path = os.path.join(parent_dir, directory)
    #
    # writer = pd.ExcelWriter(path + '/' + str(model) + '_train_stats.xlsx', engine='xlsxwriter')
    # df_train.to_excel(writer, sheet_name='summary_train')
    # writer.save()

    test_label = []
    test_seq = []
    test_desc = []
    train_iter = []
    train_sets = []
    seq_label = []
    for a in infodic['test_moves']:
        b = 'test'
        c = testseq
        d = summary['description']
        e = summary['trainiter']
        f = summary['trainsets']
        g = summary['sequence']
        test_label.append(b)
        test_seq.append(c)
        test_desc.append(d)
        train_iter.append(e)
        train_sets.append(f)
        seq_label.append(g)

    test_moves = np.array(infodic['test_moves'])
    test_gamenum = np.array(infodic['games_test'])
    test_gamescen = np.array(infodic['scen_test'])
    test_dist = np.array(infodic['test_dist'])
    description = np.array(test_desc)
    test_pattern = np.array(test_seq)
    sequence = np.array(seq_label)
    df_test = pd.DataFrame(
        {'Game_num': test_gamenum, 'Scenario': test_gamescen, 'Model': description, 'Seq #': sequence,
         'Pattern': test_pattern, 'TrainIter': train_iter,
         'TrainSets': train_sets, 'Moves': test_moves, 'Distance': test_dist})
    df_test['Avg Moves'] = df_test['Moves'].mean()

    df_test['Avg Dist'] = df_test['Distance'].mean()

    directory = str(model)
    parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results/test'
    path = os.path.join(parent_dir, directory)

    writer = pd.ExcelWriter(path + '/' + str(model) + '_test_stats.xlsx', engine='xlsxwriter')
    df_test.to_excel(writer, sheet_name='summary_test')
    writer.save()





