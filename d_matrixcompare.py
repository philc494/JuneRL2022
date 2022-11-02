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
                     'seq1_': 'seq1tmatrix.xlsx', 'seq7_': 'seq7tmatrix.xlsx'}

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

    writer = pd.ExcelWriter(savepath + file_prefix + 'tmatrixdiff.xlsx')
    result.to_excel(writer, sheet_name='summary')
    writer.save()



