import z_config
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt


def train_stats():
    # todo: make numpy arrays of data to do statistics on
    train_label = []
    for a in z_config.moves_per_train:
        b = 'train'
        train_label.append(b)
    train_name = np.array(train_label)
    train_moves = np.array(z_config.moves_per_train)
    train_gamenum = np.array(z_config.game_num_train)
    train_gamescen = np.array(z_config.scenario_per_train)
    df_train = pd.DataFrame({'Game_num': train_gamenum, 'Moves': train_moves, 'Scenario': train_gamescen, 'Type': train_name})
    df_train['MA100'] = df_train['Moves'].rolling(100).mean()

    directory = str(z_config.scenario_num)
    parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results'
    path = os.path.join(parent_dir, directory)

    writer = pd.ExcelWriter(path + '/' + z_config.scenario_num + '_train_stats.xlsx', engine='xlsxwriter')
    df_train.to_excel(writer, sheet_name='summary_train')
    writer.save()
    return df_train


def test_stats():
    # todo: make numpy arrays of data to do statistics on
    directory = str(z_config.scenario_num)
    parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results'
    path = os.path.join(parent_dir, directory)

    test_label = []
    for a in z_config.moves_per_test:
        b = 'test'
        test_label.append(b)

    test_name = np.array(test_label)
    test_moves = np.array(z_config.moves_per_test)
    # test_label = np.array(len(test_moves)
    test_gamenum = np.array(z_config.game_num_test)
    test_gamescen = np.array(z_config.scenario_per_test)
    df_test = pd.DataFrame({'Game_num': test_gamenum, 'Moves': test_moves, 'Scenario': test_gamescen, 'Type': test_name})
    df_test['MA100'] = df_test['Moves'].rolling(100).mean()

    writer = pd.ExcelWriter(path + '/' + z_config.scenario_num + '_test_stats.xlsx', engine='xlsxwriter')
    df_test.to_excel(writer, sheet_name='summary_test')
    writer.save()
    return df_test


def plot_statistics_both(train_df, test_df):
    directory = str(z_config.scenario_num)
    parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results'
    path = os.path.join(parent_dir, directory)

    combined = pd.concat([train_df, test_df]).reset_index(drop=True)
    fig = sns.relplot(data=combined, x='Game_num', y='Moves', kind='line', hue='Type', palette=['red', 'blue'])
    fig.savefig(path + '/' + z_config.scenario_num + '_' + 'traintest_graph.png')

    fig = sns.relplot(data=test_df, x='Game_num', y='Moves', kind='line', hue='Type', palette=['blue'])
    fig.savefig(path + '/' + z_config.scenario_num + '_' + 'test_graph.png')

    fig = sns.relplot(data=train_df, x='Game_num', y='Moves', kind='line', hue='Type', palette=['red'])
    fig.savefig(path + '/' + z_config.scenario_num + '_' + 'train_graph.png')


def plot_statistics_train(train_df):
    directory = str(z_config.scenario_num)
    parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results'
    path = os.path.join(parent_dir, directory)

    fig = sns.relplot(data=train_df, x='Game_num', y='Moves', kind='line', hue='Type', palette=['red'])
    fig.savefig(path + '/' + z_config.scenario_num + '_' + 'train_graph.png')
