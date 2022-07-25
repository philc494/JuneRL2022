import pandas as pd
import numpy as np
import os
import seaborn as sns


def stats(model, resultsdic):
    train_label = []
    for a in resultsdic[model]['train_moves']:
        b = 'train'
        train_label.append(b)
    train_name = np.array(train_label)
    train_moves = np.array(resultsdic[model]['train_moves'])
    train_gamenum = np.array(resultsdic[model]['games_train'])
    train_gamescen = np.array(resultsdic[model]['scen_train'])
    df_train = pd.DataFrame({'Game_num': train_gamenum, 'Moves': train_moves, 'Scenario': train_gamescen, 'Type': train_name})
    df_train['MA100'] = df_train['Moves'].rolling(100).mean()

    directory = str(model)
    parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results'
    path = os.path.join(parent_dir, directory)

    writer = pd.ExcelWriter(path + '/' + str(model) + '_train_stats.xlsx', engine='xlsxwriter')
    df_train.to_excel(writer, sheet_name='summary_train')
    writer.save()

    test_label = []
    for a in resultsdic[model]['test_moves']:
        b = 'test'
        test_label.append(b)
    test_name = np.array(test_label)
    test_moves = np.array(resultsdic[model]['test_moves'])
    test_gamenum = np.array(resultsdic[model]['games_test'])
    test_gamescen = np.array(resultsdic[model]['scen_test'])
    df_test = pd.DataFrame(
        {'Game_num': test_gamenum, 'Moves': test_moves, 'Scenario': test_gamescen, 'Type': test_name})
    df_test['MA100'] = df_test['Moves'].rolling(100).mean()

    directory = str(model)
    parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results'
    path = os.path.join(parent_dir, directory)

    writer = pd.ExcelWriter(path + '/' + str(model) + '_test_stats.xlsx', engine='xlsxwriter')
    df_train.to_excel(writer, sheet_name='summary_test')
    writer.save()

    combined = pd.concat([df_train, df_test]).reset_index(drop=True)
    fig = sns.relplot(data=combined, x='Game_num', y='Moves', kind='line', hue='Type', palette=['red', 'blue'])
    fig.savefig(path + '/' + str(model) + '_' + 'traintest_graph.png')

    fig = sns.relplot(data=df_test, x='Game_num', y='Moves', kind='line', hue='Type', palette=['blue'])
    fig.savefig(path + '/' + str(model) + '_' + 'test_graph.png')

    fig = sns.relplot(data=df_train, x='Game_num', y='Moves', kind='line', hue='Type', palette=['red'])
    fig.savefig(path + '/' + str(model) + '_' + 'train_graph.png')
    return {'train': df_train, 'test': df_test}



