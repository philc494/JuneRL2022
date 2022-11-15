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
    Adown_prob = df.iat[0, 4]
    Aleft_prob = df.iat[0, 5]
    Amid_prob = df.iat[0, 6]
    Aright_prob = df.iat[0, 7]
    Aup_prob = df.iat[0, 8]

    BA_prob = df.iat[1, 0]
    BB_prob = df.iat[1, 1]
    BC_prob = df.iat[1, 2]
    BD_prob = df.iat[1, 3]
    Bdown_prob = df.iat[1, 4]
    Bleft_prob = df.iat[1, 5]
    Bmid_prob = df.iat[1, 6]
    Bright_prob = df.iat[1, 7]
    Bup_prob = df.iat[1, 8]

    CA_prob = df.iat[2, 0]
    CB_prob = df.iat[2, 1]
    CC_prob = df.iat[2, 2]
    CD_prob = df.iat[2, 3]
    Cdown_prob = df.iat[2, 4]
    Cleft_prob = df.iat[2, 5]
    Cmid_prob = df.iat[2, 6]
    Cright_prob = df.iat[2, 7]
    Cup_prob = df.iat[2, 8]

    DA_prob = df.iat[3, 0]
    DB_prob = df.iat[3, 1]
    DC_prob = df.iat[3, 2]
    DD_prob = df.iat[3, 3]
    Ddown_prob = df.iat[3, 4]
    Dleft_prob = df.iat[3, 5]
    Dmid_prob = df.iat[3, 6]
    Dright_prob = df.iat[3, 7]
    Dup_prob = df.iat[3, 8]

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
            int_A_test[0, 2][(i, j)] = round(Aup_prob, 3)
            int_A_test[0, 3][(i, j)] = round(AB_prob, 3)
            int_A_test[0, 4][(i, j)] = round(AB_prob, 3)

            int_A_test[1, 0][(i, j)] = round(AA_prob, 3)
            int_A_test[1, 1][(i, j)] = round(AA_prob, 3)
            int_A_test[1, 2][(i, j)] = round(Aup_prob, 3)
            int_A_test[1, 3][(i, j)] = round(AB_prob, 3)
            int_A_test[1, 4][(i, j)] = round(AB_prob, 3)

            int_A_test[2, 0][(i, j)] = round(Aleft_prob, 3)
            int_A_test[2, 1][(i, j)] = round(Aleft_prob, 3)
            int_A_test[2, 2][(i, j)] = round(Amid_prob, 3)
            int_A_test[2, 3][(i, j)] = round(Aright_prob, 3)
            int_A_test[2, 4][(i, j)] = round(Aright_prob, 3)

            int_A_test[3, 0][(i, j)] = round(AC_prob, 3)
            int_A_test[3, 1][(i, j)] = round(AC_prob, 3)
            int_A_test[3, 2][(i, j)] = round(Adown_prob, 3)
            int_A_test[3, 3][(i, j)] = round(AD_prob, 3)
            int_A_test[3, 4][(i, j)] = round(AD_prob, 3)

            int_A_test[4, 0][(i, j)] = round(AC_prob, 3)
            int_A_test[4, 1][(i, j)] = round(AC_prob, 3)
            int_A_test[4, 2][(i, j)] = round(Adown_prob, 3)
            int_A_test[4, 3][(i, j)] = round(AD_prob, 3)
            int_A_test[4, 4][(i, j)] = round(AD_prob, 3)

            int_B_test[0, 0][(i, j)] = round(BA_prob, 3)
            int_B_test[0, 1][(i, j)] = round(BA_prob, 3)
            int_B_test[0, 2][(i, j)] = round(Bup_prob, 3)
            int_B_test[0, 3][(i, j)] = round(BB_prob, 3)
            int_B_test[0, 4][(i, j)] = round(BB_prob, 3)

            int_B_test[1, 0][(i, j)] = round(BA_prob, 3)
            int_B_test[1, 1][(i, j)] = round(BA_prob, 3)
            int_B_test[1, 2][(i, j)] = round(Bup_prob, 3)
            int_B_test[1, 3][(i, j)] = round(BB_prob, 3)
            int_B_test[1, 4][(i, j)] = round(BB_prob, 3)

            int_B_test[2, 0][(i, j)] = round(Bleft_prob, 3)
            int_B_test[2, 1][(i, j)] = round(Bleft_prob, 3)
            int_B_test[2, 2][(i, j)] = round(Bmid_prob, 3)
            int_B_test[2, 3][(i, j)] = round(Bright_prob, 3)
            int_B_test[2, 4][(i, j)] = round(Bright_prob, 3)

            int_B_test[3, 0][(i, j)] = round(BC_prob, 3)
            int_B_test[3, 1][(i, j)] = round(BC_prob, 3)
            int_B_test[3, 2][(i, j)] = round(Bdown_prob, 3)
            int_B_test[3, 3][(i, j)] = round(BD_prob, 3)
            int_B_test[3, 4][(i, j)] = round(BD_prob, 3)

            int_B_test[4, 0][(i, j)] = round(BC_prob, 3)
            int_B_test[4, 1][(i, j)] = round(BC_prob, 3)
            int_B_test[4, 2][(i, j)] = round(Bdown_prob, 3)
            int_B_test[4, 3][(i, j)] = round(BD_prob, 3)
            int_B_test[4, 4][(i, j)] = round(BD_prob, 3)

            int_C_test[0, 0][(i, j)] = round(CA_prob, 3)
            int_C_test[0, 1][(i, j)] = round(CA_prob, 3)
            int_C_test[0, 2][(i, j)] = round(Cup_prob, 3)
            int_C_test[0, 3][(i, j)] = round(CB_prob, 3)
            int_C_test[0, 4][(i, j)] = round(CB_prob, 3)

            int_C_test[1, 0][(i, j)] = round(CA_prob, 3)
            int_C_test[1, 1][(i, j)] = round(CA_prob, 3)
            int_C_test[1, 2][(i, j)] = round(Cup_prob, 3)
            int_C_test[1, 3][(i, j)] = round(CB_prob, 3)
            int_C_test[1, 4][(i, j)] = round(CB_prob, 3)

            int_C_test[2, 0][(i, j)] = round(Cleft_prob, 3)
            int_C_test[2, 1][(i, j)] = round(Cleft_prob, 3)
            int_C_test[2, 2][(i, j)] = round(Cmid_prob, 3)
            int_C_test[2, 3][(i, j)] = round(Cright_prob, 3)
            int_C_test[2, 4][(i, j)] = round(Cright_prob, 3)

            int_C_test[3, 0][(i, j)] = round(CC_prob, 3)
            int_C_test[3, 1][(i, j)] = round(CC_prob, 3)
            int_C_test[3, 2][(i, j)] = round(Cdown_prob, 3)
            int_C_test[3, 3][(i, j)] = round(CD_prob, 3)
            int_C_test[3, 4][(i, j)] = round(CD_prob, 3)

            int_C_test[4, 0][(i, j)] = round(CC_prob, 3)
            int_C_test[4, 1][(i, j)] = round(CC_prob, 3)
            int_C_test[4, 2][(i, j)] = round(Cdown_prob, 3)
            int_C_test[4, 3][(i, j)] = round(CD_prob, 3)
            int_C_test[4, 4][(i, j)] = round(CD_prob, 3)

            int_D_test[0, 0][(i, j)] = round(DA_prob, 3)
            int_D_test[0, 1][(i, j)] = round(DA_prob, 3)
            int_D_test[0, 2][(i, j)] = round(Dup_prob, 3)
            int_D_test[0, 3][(i, j)] = round(DB_prob, 3)
            int_D_test[0, 4][(i, j)] = round(DB_prob, 3)

            int_D_test[1, 0][(i, j)] = round(DA_prob, 3)
            int_D_test[1, 1][(i, j)] = round(DA_prob, 3)
            int_D_test[1, 2][(i, j)] = round(Dup_prob, 3)
            int_D_test[1, 3][(i, j)] = round(DB_prob, 3)
            int_D_test[1, 4][(i, j)] = round(DB_prob, 3)

            int_D_test[2, 0][(i, j)] = round(Dleft_prob, 3)
            int_D_test[2, 1][(i, j)] = round(Dleft_prob, 3)
            int_D_test[2, 2][(i, j)] = round(Dmid_prob, 3)
            int_D_test[2, 3][(i, j)] = round(Dright_prob, 3)
            int_D_test[2, 4][(i, j)] = round(Dright_prob, 3)

            int_D_test[3, 0][(i, j)] = round(DC_prob, 3)
            int_D_test[3, 1][(i, j)] = round(DC_prob, 3)
            int_D_test[3, 2][(i, j)] = round(Ddown_prob, 3)
            int_D_test[3, 3][(i, j)] = round(DD_prob, 3)
            int_D_test[3, 4][(i, j)] = round(DD_prob, 3)

            int_D_test[4, 0][(i, j)] = round(DC_prob, 3)
            int_D_test[4, 1][(i, j)] = round(DC_prob, 3)
            int_D_test[4, 2][(i, j)] = round(Ddown_prob, 3)
            int_D_test[4, 3][(i, j)] = round(DD_prob, 3)
            int_D_test[4, 4][(i, j)] = round(DD_prob, 3)

    metatestdic = {'Aint': int_A_test, 'Bint': int_B_test, 'Dint': int_D_test, 'Cint': int_C_test}
    visualize_testtables(model, metatestdic, label)









