import pandas as pd
import os

path = '/Users/philcrawford/PycharmProjects/JuneRL2022/results/test/1/'
savepath = '/Users/philcrawford/PycharmProjects/JuneRL2022/results/general/'

main_matrix = 'testmatrix'
main_matrix_loc = path + main_matrix + '.xlsx'

test_matrix_list = []

act_matrix = {'cust1': 'cust1tmatrix.xlsx', 'cust2': 'cust2tmatrix.xlsx',
                     'cust3': 'cust3tmatrix.xlsx', 'cust4': 'cust4tmatrix.xlsx',
                     'cust5': 'cust5tmatrix.xlsx', 'cust6': 'cust6tmatrix.xlsx',
                     'seq1_': 'seq1tmatrix.xlsx', 'seq3_': 'seq3tmatrix.xlsx',
              'seq7_': 'seq7tmatrix.xlsx'}

for file in os.listdir(path):
    if file.__contains__('tmatrix'):
        test_matrix_list.append(file)

for file in test_matrix_list:
    matrix = path + file
    testmatrix = pd.read_excel(matrix, index_col=0)
    file_prefix = file[0:12]
    file_dic = file[7:12]
    actual_mat = savepath + act_matrix[file_dic]
    actualmatrix = pd.read_excel(actual_mat, index_col=0)
    result = testmatrix - actualmatrix
    result.at['A', 'Down'] = testmatrix.at['A', 'Down']
    result.at['A', 'Left'] = testmatrix.at['A', 'Left']
    result.at['A', 'Mid'] = testmatrix.at['A', 'Mid']
    result.at['A', 'Right'] = testmatrix.at['A', 'Right']
    result.at['A', 'Up'] = testmatrix.at['A', 'Up']

    result.at['B', 'Down'] = testmatrix.at['B', 'Down']
    result.at['B', 'Left'] = testmatrix.at['B', 'Left']
    result.at['B', 'Mid'] = testmatrix.at['B', 'Mid']
    result.at['B', 'Right'] = testmatrix.at['B', 'Right']
    result.at['B', 'Up'] = testmatrix.at['B', 'Up']

    result.at['C', 'Down'] = testmatrix.at['C', 'Down']
    result.at['C', 'Left'] = testmatrix.at['C', 'Left']
    result.at['C', 'Mid'] = testmatrix.at['C', 'Mid']
    result.at['C', 'Right'] = testmatrix.at['C', 'Right']
    result.at['C', 'Up'] = testmatrix.at['C', 'Up']

    result.at['D', 'Down'] = testmatrix.at['D', 'Down']
    result.at['D', 'Left'] = testmatrix.at['D', 'Left']
    result.at['D', 'Mid'] = testmatrix.at['D', 'Mid']
    result.at['D', 'Right'] = testmatrix.at['D', 'Right']
    result.at['D', 'Up'] = testmatrix.at['D', 'Up']

    writer = pd.ExcelWriter(savepath + 'diff_' + file + 'tmatrixdiff.xlsx')
    result.to_excel(writer, sheet_name='summary')
    writer.save()



