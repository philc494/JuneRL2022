import pandas as pd
import os
from z_diffvisualization import visualize_testtables

board_rows = 5
board_cols = 5

model = '1'
path = '/Users/philcrawford/PycharmProjects/JuneRL2022/results/general/diffmatrices/' + model + '/'

for file in os.listdir(path):
    label = file[0:25]
    matrix = path + file
    df = pd.read_excel(matrix, index_col=0)

    AA_prob = df.iat[0, 0]
    AB_prob = df.iat[0, 1]
    AC_prob = df.iat[0, 2]
    AD_prob = df.iat[0, 3]

    BA_prob = df.iat[1, 0]
    BB_prob = df.iat[1, 1]
    BC_prob = df.iat[1, 2]
    BD_prob = df.iat[1, 3]

    CA_prob = df.iat[2, 0]
    CB_prob = df.iat[2, 1]
    CC_prob = df.iat[2, 2]
    CD_prob = df.iat[2, 3]

    DA_prob = df.iat[3, 0]
    DB_prob = df.iat[3, 1]
    DC_prob = df.iat[3, 2]
    DD_prob = df.iat[3, 3]

    int_A_test = {}
    int_B_test = {}
    int_C_test = {}
    int_D_test = {}

    for i in range(board_rows):
        for j in range(board_cols):
            int_A_test[(i, j)] = {}
            int_B_test[(i, j)] = {}
            int_C_test[(i, j)] = {}
            int_D_test[(i, j)] = {}

    for i in range(-1, 2):
        for j in range(-1, 2):
            int_A_test[0, 0][(i, j)] = round(AA_prob, 3)
            int_A_test[0, 1][(i, j)] = round(AA_prob, 3)
            int_A_test[0, 2][(i, j)] = 0
            int_A_test[0, 3][(i, j)] = round(AB_prob, 3)
            int_A_test[0, 4][(i, j)] = round(AB_prob, 3)

            int_A_test[1, 0][(i, j)] = round(AA_prob, 3)
            int_A_test[1, 1][(i, j)] = round(AA_prob, 3)
            int_A_test[1, 2][(i, j)] = 0
            int_A_test[1, 3][(i, j)] = round(AB_prob, 3)
            int_A_test[1, 4][(i, j)] = round(AB_prob, 3)

            int_A_test[2, 0][(i, j)] = 0
            int_A_test[2, 1][(i, j)] = 0
            int_A_test[2, 2][(i, j)] = 0
            int_A_test[2, 3][(i, j)] = 0
            int_A_test[2, 4][(i, j)] = 0

            int_A_test[3, 0][(i, j)] = round(AC_prob, 3)
            int_A_test[3, 1][(i, j)] = round(AC_prob, 3)
            int_A_test[3, 2][(i, j)] = 0
            int_A_test[3, 3][(i, j)] = round(AD_prob, 3)
            int_A_test[3, 4][(i, j)] = round(AD_prob, 3)

            int_A_test[4, 0][(i, j)] = round(AC_prob, 3)
            int_A_test[4, 1][(i, j)] = round(AC_prob, 3)
            int_A_test[4, 2][(i, j)] = 0
            int_A_test[4, 3][(i, j)] = round(AD_prob, 3)
            int_A_test[4, 4][(i, j)] = round(AD_prob, 3)

            int_B_test[0, 0][(i, j)] = round(BA_prob, 3)
            int_B_test[0, 1][(i, j)] = round(BA_prob, 3)
            int_B_test[0, 2][(i, j)] = 0
            int_B_test[0, 3][(i, j)] = round(BB_prob, 3)
            int_B_test[0, 4][(i, j)] = round(BB_prob, 3)

            int_B_test[1, 0][(i, j)] = round(BA_prob, 3)
            int_B_test[1, 1][(i, j)] = round(BA_prob, 3)
            int_B_test[1, 2][(i, j)] = 0
            int_B_test[1, 3][(i, j)] = round(BB_prob, 3)
            int_B_test[1, 4][(i, j)] = round(BB_prob, 3)

            int_B_test[2, 0][(i, j)] = 0
            int_B_test[2, 1][(i, j)] = 0
            int_B_test[2, 2][(i, j)] = 0
            int_B_test[2, 3][(i, j)] = 0
            int_B_test[2, 4][(i, j)] = 0

            int_B_test[3, 0][(i, j)] = round(BC_prob, 3)
            int_B_test[3, 1][(i, j)] = round(BC_prob, 3)
            int_B_test[3, 2][(i, j)] = 0
            int_B_test[3, 3][(i, j)] = round(BD_prob, 3)
            int_B_test[3, 4][(i, j)] = round(BD_prob, 3)

            int_B_test[4, 0][(i, j)] = round(BC_prob, 3)
            int_B_test[4, 1][(i, j)] = round(BC_prob, 3)
            int_B_test[4, 2][(i, j)] = 0
            int_B_test[4, 3][(i, j)] = round(BD_prob, 3)
            int_B_test[4, 4][(i, j)] = round(BD_prob, 3)

            int_C_test[0, 0][(i, j)] = round(CA_prob, 3)
            int_C_test[0, 1][(i, j)] = round(CA_prob, 3)
            int_C_test[0, 2][(i, j)] = 0
            int_C_test[0, 3][(i, j)] = round(CB_prob, 3)
            int_C_test[0, 4][(i, j)] = round(CB_prob, 3)

            int_C_test[1, 0][(i, j)] = round(CA_prob, 3)
            int_C_test[1, 1][(i, j)] = round(CA_prob, 3)
            int_C_test[1, 2][(i, j)] = 0
            int_C_test[1, 3][(i, j)] = round(CB_prob, 3)
            int_C_test[1, 4][(i, j)] = round(CB_prob, 3)

            int_C_test[2, 0][(i, j)] = 0
            int_C_test[2, 1][(i, j)] = 0
            int_C_test[2, 2][(i, j)] = 0
            int_C_test[2, 3][(i, j)] = 0
            int_C_test[2, 4][(i, j)] = 0

            int_C_test[3, 0][(i, j)] = round(CC_prob, 3)
            int_C_test[3, 1][(i, j)] = round(CC_prob, 3)
            int_C_test[3, 2][(i, j)] = 0
            int_C_test[3, 3][(i, j)] = round(CD_prob, 3)
            int_C_test[3, 4][(i, j)] = round(CD_prob, 3)

            int_C_test[4, 0][(i, j)] = round(CC_prob, 3)
            int_C_test[4, 1][(i, j)] = round(CC_prob, 3)
            int_C_test[4, 2][(i, j)] = 0
            int_C_test[4, 3][(i, j)] = round(CD_prob, 3)
            int_C_test[4, 4][(i, j)] = round(CD_prob, 3)

            int_D_test[0, 0][(i, j)] = round(DA_prob, 3)
            int_D_test[0, 1][(i, j)] = round(DA_prob, 3)
            int_D_test[0, 2][(i, j)] = 0
            int_D_test[0, 3][(i, j)] = round(DB_prob, 3)
            int_D_test[0, 4][(i, j)] = round(DB_prob, 3)

            int_D_test[1, 0][(i, j)] = round(DA_prob, 3)
            int_D_test[1, 1][(i, j)] = round(DA_prob, 3)
            int_D_test[1, 2][(i, j)] = 0
            int_D_test[1, 3][(i, j)] = round(DB_prob, 3)
            int_D_test[1, 4][(i, j)] = round(DB_prob, 3)

            int_D_test[2, 0][(i, j)] = 0
            int_D_test[2, 1][(i, j)] = 0
            int_D_test[2, 2][(i, j)] = 0
            int_D_test[2, 3][(i, j)] = 0
            int_D_test[2, 4][(i, j)] = 0

            int_D_test[3, 0][(i, j)] = round(DC_prob, 3)
            int_D_test[3, 1][(i, j)] = round(DC_prob, 3)
            int_D_test[3, 2][(i, j)] = 0
            int_D_test[3, 3][(i, j)] = round(DD_prob, 3)
            int_D_test[3, 4][(i, j)] = round(DD_prob, 3)

            int_D_test[4, 0][(i, j)] = round(DC_prob, 3)
            int_D_test[4, 1][(i, j)] = round(DC_prob, 3)
            int_D_test[4, 2][(i, j)] = 0
            int_D_test[4, 3][(i, j)] = round(DD_prob, 3)
            int_D_test[4, 4][(i, j)] = round(DD_prob, 3)

    metatestdic = {'Aint': int_A_test, 'Bint': int_B_test, 'Dint': int_D_test, 'Cint': int_C_test}
    visualize_testtables(model, metatestdic, label)









