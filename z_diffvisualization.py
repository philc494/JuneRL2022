import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def minisquare_values(reward_dic, board_pos):
    mini_dic = {}
    for i in range(-1, 2):
        for j in range(-1, 2):
            mini_dic[(i, j)] = (reward_dic[board_pos][(i, j)])
    return mini_dic


def visualize_testtables(model, resultsdic, label):
    reward_info_out = {"intA": [resultsdic["Aint"], "AAint_rewards", "AAint"],
                       "intB": [resultsdic["Bint"], "BBint_rewards", "BBint"],
                       "intC": [resultsdic["Cint"], "CCint_rewards", "CCint"],
                       "intD": [resultsdic["Dint"], "DDint_rewards", "DDint"]}

    for a in reward_info_out:
        dic_value_list = []
        for b in reward_info_out[a][0]:
            for c in reward_info_out[a][0][b]:
                dic_value_list.append(reward_info_out[a][0][b][c])
        min_val = min(dic_value_list)
        max_val = max(dic_value_list)
        dic00 = minisquare_values(reward_info_out[a][0], (0, 0))
        v00_n1n1 = dic00[(-1, -1)]
        v00_n10 = dic00[(-1, 0)]
        v00_n11 = dic00[(-1, 1)]
        v00_0n1 = dic00[(0, -1)]
        v00_00 = dic00[(0, 0)]
        v00_01 = dic00[(0, 1)]
        v00_1n1 = dic00[(1, -1)]
        v00_10 = dic00[(1, 0)]
        v00_11 = dic00[(1, 1)]
        dic01 = minisquare_values(reward_info_out[a][0], (0, 1))

        v01_n1n1 = dic01[(-1, -1)]
        v01_n10 = dic01[(-1, 0)]
        v01_n11 = dic01[(-1, 1)]
        v01_0n1 = dic01[(0, -1)]
        v01_00 = dic01[(0, 0)]
        v01_01 = dic01[(0, 1)]
        v01_1n1 = dic01[(1, -1)]
        v01_10 = dic01[(1, 0)]
        v01_11 = dic01[(1, 1)]
        dic02 = minisquare_values(reward_info_out[a][0], (0, 2))

        v02_n1n1 = dic02[(-1, -1)]
        v02_n10 = dic02[(-1, 0)]
        v02_n11 = dic02[(-1, 1)]
        v02_0n1 = dic02[(0, -1)]
        v02_00 = dic02[(0, 0)]
        v02_01 = dic02[(0, 1)]
        v02_1n1 = dic02[(1, -1)]
        v02_10 = dic02[(1, 0)]
        v02_11 = dic02[(1, 1)]
        dic03 = minisquare_values(reward_info_out[a][0], (0, 3))

        v03_n1n1 = dic03[(-1, -1)]
        v03_n10 = dic03[(-1, 0)]
        v03_n11 = dic03[(-1, 1)]
        v03_0n1 = dic03[(0, -1)]
        v03_00 = dic03[(0, 0)]
        v03_01 = dic03[(0, 1)]
        v03_1n1 = dic03[(1, -1)]
        v03_10 = dic03[(1, 0)]
        v03_11 = dic03[(1, 1)]
        dic04 = minisquare_values(reward_info_out[a][0], (0, 4))

        v04_n1n1 = dic04[(-1, -1)]
        v04_n10 = dic04[(-1, 0)]
        v04_n11 = dic04[(-1, 1)]
        v04_0n1 = dic04[(0, -1)]
        v04_00 = dic04[(0, 0)]
        v04_01 = dic04[(0, 1)]
        v04_1n1 = dic04[(1, -1)]
        v04_10 = dic04[(1, 0)]
        v04_11 = dic04[(1, 1)]
        dic10 = minisquare_values(reward_info_out[a][0], (1, 0))

        v10_n1n1 = dic10[(-1, -1)]
        v10_n10 = dic10[(-1, 0)]
        v10_n11 = dic10[(-1, 1)]
        v10_0n1 = dic10[(0, -1)]
        v10_00 = dic10[(0, 0)]
        v10_01 = dic10[(0, 1)]
        v10_1n1 = dic10[(1, -1)]
        v10_10 = dic10[(1, 0)]
        v10_11 = dic10[(1, 1)]
        dic11 = minisquare_values(reward_info_out[a][0], (1, 1))

        v11_n1n1 = dic11[(-1, -1)]
        v11_n10 = dic11[(-1, 0)]
        v11_n11 = dic11[(-1, 1)]
        v11_0n1 = dic11[(0, -1)]
        v11_00 = dic11[(0, 0)]
        v11_01 = dic11[(0, 1)]
        v11_1n1 = dic11[(1, -1)]
        v11_10 = dic11[(1, 0)]
        v11_11 = dic11[(1, 1)]
        dic12 = minisquare_values(reward_info_out[a][0], (1, 2))

        v12_n1n1 = dic12[(-1, -1)]
        v12_n10 = dic12[(-1, 0)]
        v12_n11 = dic12[(-1, 1)]
        v12_0n1 = dic12[(0, -1)]
        v12_00 = dic12[(0, 0)]
        v12_01 = dic12[(0, 1)]
        v12_1n1 = dic12[(1, -1)]
        v12_10 = dic12[(1, 0)]
        v12_11 = dic12[(1, 1)]
        dic13 = minisquare_values(reward_info_out[a][0], (1, 3))

        v13_n1n1 = dic13[(-1, -1)]
        v13_n10 = dic13[(-1, 0)]
        v13_n11 = dic13[(-1, 1)]
        v13_0n1 = dic13[(0, -1)]
        v13_00 = dic13[(0, 0)]
        v13_01 = dic13[(0, 1)]
        v13_1n1 = dic13[(1, -1)]
        v13_10 = dic13[(1, 0)]
        v13_11 = dic13[(1, 1)]
        dic14 = minisquare_values(reward_info_out[a][0], (1, 4))

        v14_n1n1 = dic14[(-1, -1)]
        v14_n10 = dic14[(-1, 0)]
        v14_n11 = dic14[(-1, 1)]
        v14_0n1 = dic14[(0, -1)]
        v14_00 = dic14[(0, 0)]
        v14_01 = dic14[(0, 1)]
        v14_1n1 = dic14[(1, -1)]
        v14_10 = dic14[(1, 0)]
        v14_11 = dic14[(1, 1)]
        dic20 = minisquare_values(reward_info_out[a][0], (2, 0))

        v20_n1n1 = dic20[(-1, -1)]
        v20_n10 = dic20[(-1, 0)]
        v20_n11 = dic20[(-1, 1)]
        v20_0n1 = dic20[(0, -1)]
        v20_00 = dic20[(0, 0)]
        v20_01 = dic20[(0, 1)]
        v20_1n1 = dic20[(1, -1)]
        v20_10 = dic20[(1, 0)]
        v20_11 = dic20[(1, 1)]
        dic21 = minisquare_values(reward_info_out[a][0], (2, 1))

        v21_n1n1 = dic21[(-1, -1)]
        v21_n10 = dic21[(-1, 0)]
        v21_n11 = dic21[(-1, 1)]
        v21_0n1 = dic21[(0, -1)]
        v21_00 = dic21[(0, 0)]
        v21_01 = dic21[(0, 1)]
        v21_1n1 = dic21[(1, -1)]
        v21_10 = dic21[(1, 0)]
        v21_11 = dic21[(1, 1)]
        dic22 = minisquare_values(reward_info_out[a][0], (2, 2))

        v22_n1n1 = dic22[(-1, -1)]
        v22_n10 = dic22[(-1, 0)]
        v22_n11 = dic22[(-1, 1)]
        v22_0n1 = dic22[(0, -1)]
        v22_00 = dic22[(0, 0)]
        v22_01 = dic22[(0, 1)]
        v22_1n1 = dic22[(1, -1)]
        v22_10 = dic22[(1, 0)]
        v22_11 = dic22[(1, 1)]
        dic23 = minisquare_values(reward_info_out[a][0], (2, 3))

        v23_n1n1 = dic23[(-1, -1)]
        v23_n10 = dic23[(-1, 0)]
        v23_n11 = dic23[(-1, 1)]
        v23_0n1 = dic23[(0, -1)]
        v23_00 = dic23[(0, 0)]
        v23_01 = dic23[(0, 1)]
        v23_1n1 = dic23[(1, -1)]
        v23_10 = dic23[(1, 0)]
        v23_11 = dic23[(1, 1)]
        dic24 = minisquare_values(reward_info_out[a][0], (2, 4))

        v24_n1n1 = dic24[(-1, -1)]
        v24_n10 = dic24[(-1, 0)]
        v24_n11 = dic24[(-1, 1)]
        v24_0n1 = dic24[(0, -1)]
        v24_00 = dic24[(0, 0)]
        v24_01 = dic24[(0, 1)]
        v24_1n1 = dic24[(1, -1)]
        v24_10 = dic24[(1, 0)]
        v24_11 = dic24[(1, 1)]
        dic30 = minisquare_values(reward_info_out[a][0], (3, 0))

        v30_n1n1 = dic30[(-1, -1)]
        v30_n10 = dic30[(-1, 0)]
        v30_n11 = dic30[(-1, 1)]
        v30_0n1 = dic30[(0, -1)]
        v30_00 = dic30[(0, 0)]
        v30_01 = dic30[(0, 1)]
        v30_1n1 = dic30[(1, -1)]
        v30_10 = dic30[(1, 0)]
        v30_11 = dic30[(1, 1)]
        dic31 = minisquare_values(reward_info_out[a][0], (3, 1))

        v31_n1n1 = dic31[(-1, -1)]
        v31_n10 = dic31[(-1, 0)]
        v31_n11 = dic31[(-1, 1)]
        v31_0n1 = dic31[(0, -1)]
        v31_00 = dic31[(0, 0)]
        v31_01 = dic31[(0, 1)]
        v31_1n1 = dic31[(1, -1)]
        v31_10 = dic31[(1, 0)]
        v31_11 = dic31[(1, 1)]
        dic32 = minisquare_values(reward_info_out[a][0], (3, 2))

        v32_n1n1 = dic32[(-1, -1)]
        v32_n10 = dic32[(-1, 0)]
        v32_n11 = dic32[(-1, 1)]
        v32_0n1 = dic32[(0, -1)]
        v32_00 = dic32[(0, 0)]
        v32_01 = dic32[(0, 1)]
        v32_1n1 = dic32[(1, -1)]
        v32_10 = dic32[(1, 0)]
        v32_11 = dic32[(1, 1)]
        dic33 = minisquare_values(reward_info_out[a][0], (3, 3))

        v33_n1n1 = dic33[(-1, -1)]
        v33_n10 = dic33[(-1, 0)]
        v33_n11 = dic33[(-1, 1)]
        v33_0n1 = dic33[(0, -1)]
        v33_00 = dic33[(0, 0)]
        v33_01 = dic33[(0, 1)]
        v33_1n1 = dic33[(1, -1)]
        v33_10 = dic33[(1, 0)]
        v33_11 = dic33[(1, 1)]
        dic34 = minisquare_values(reward_info_out[a][0], (3, 4))

        v34_n1n1 = dic34[(-1, -1)]
        v34_n10 = dic34[(-1, 0)]
        v34_n11 = dic34[(-1, 1)]
        v34_0n1 = dic34[(0, -1)]
        v34_00 = dic34[(0, 0)]
        v34_01 = dic34[(0, 1)]
        v34_1n1 = dic34[(1, -1)]
        v34_10 = dic34[(1, 0)]
        v34_11 = dic34[(1, 1)]
        dic40 = minisquare_values(reward_info_out[a][0], (4, 0))

        v40_n1n1 = dic40[(-1, -1)]
        v40_n10 = dic40[(-1, 0)]
        v40_n11 = dic40[(-1, 1)]
        v40_0n1 = dic40[(0, -1)]
        v40_00 = dic40[(0, 0)]
        v40_01 = dic40[(0, 1)]
        v40_1n1 = dic40[(1, -1)]
        v40_10 = dic40[(1, 0)]
        v40_11 = dic40[(1, 1)]
        dic41 = minisquare_values(reward_info_out[a][0], (4, 1))

        v41_n1n1 = dic41[(-1, -1)]
        v41_n10 = dic41[(-1, 0)]
        v41_n11 = dic41[(-1, 1)]
        v41_0n1 = dic41[(0, -1)]
        v41_00 = dic41[(0, 0)]
        v41_01 = dic41[(0, 1)]
        v41_1n1 = dic41[(1, -1)]
        v41_10 = dic41[(1, 0)]
        v41_11 = dic41[(1, 1)]
        dic42 = minisquare_values(reward_info_out[a][0], (4, 2))

        v42_n1n1 = dic42[(-1, -1)]
        v42_n10 = dic42[(-1, 0)]
        v42_n11 = dic42[(-1, 1)]
        v42_0n1 = dic42[(0, -1)]
        v42_00 = dic42[(0, 0)]
        v42_01 = dic42[(0, 1)]
        v42_1n1 = dic42[(1, -1)]
        v42_10 = dic42[(1, 0)]
        v42_11 = dic42[(1, 1)]
        dic43 = minisquare_values(reward_info_out[a][0], (4, 3))

        v43_n1n1 = dic43[(-1, -1)]
        v43_n10 = dic43[(-1, 0)]
        v43_n11 = dic43[(-1, 1)]
        v43_0n1 = dic43[(0, -1)]
        v43_00 = dic43[(0, 0)]
        v43_01 = dic43[(0, 1)]
        v43_1n1 = dic43[(1, -1)]
        v43_10 = dic43[(1, 0)]
        v43_11 = dic43[(1, 1)]
        dic44 = minisquare_values(reward_info_out[a][0], (4, 4))

        v44_n1n1 = dic44[(-1, -1)]
        v44_n10 = dic44[(-1, 0)]
        v44_n11 = dic44[(-1, 1)]
        v44_0n1 = dic44[(0, -1)]
        v44_00 = dic44[(0, 0)]
        v44_01 = dic44[(0, 1)]
        v44_1n1 = dic44[(1, -1)]
        v44_10 = dic44[(1, 0)]
        v44_11 = dic44[(1, 1)]

        df00 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v00_n1n1, v00_n10, v00_n11, v00_0n1, v00_00, v00_01, v00_1n1, v00_10, v00_11]})
        df01 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v01_n1n1, v01_n10, v01_n11, v01_0n1, v01_00, v01_01, v01_1n1, v01_10, v01_11]})
        df02 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v02_n1n1, v02_n10, v02_n11, v02_0n1, v02_00, v02_01, v02_1n1, v02_10, v02_11]})
        df03 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v03_n1n1, v03_n10, v03_n11, v03_0n1, v03_00, v03_01, v03_1n1, v03_10, v03_11]})
        df04 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v04_n1n1, v04_n10, v04_n11, v04_0n1, v04_00, v04_01, v04_1n1, v04_10, v04_11]})
        df10 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v10_n1n1, v10_n10, v10_n11, v10_0n1, v10_00, v10_01, v10_1n1, v10_10, v10_11]})
        df11 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v11_n1n1, v11_n10, v11_n11, v11_0n1, v11_00, v11_01, v11_1n1, v11_10, v11_11]})
        df12 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v12_n1n1, v12_n10, v12_n11, v12_0n1, v12_00, v12_01, v12_1n1, v12_10, v12_11]})
        df13 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v13_n1n1, v13_n10, v13_n11, v13_0n1, v13_00, v13_01, v13_1n1, v13_10, v13_11]})
        df14 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v14_n1n1, v14_n10, v14_n11, v14_0n1, v14_00, v14_01, v14_1n1, v14_10, v14_11]})
        df20 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v20_n1n1, v20_n10, v20_n11, v20_0n1, v20_00, v20_01, v20_1n1, v20_10, v20_11]})
        df21 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v21_n1n1, v21_n10, v21_n11, v21_0n1, v21_00, v21_01, v21_1n1, v21_10, v21_11]})
        df22 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v22_n1n1, v22_n10, v22_n11, v22_0n1, v22_00, v22_01, v22_1n1, v22_10, v22_11]})
        df23 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v23_n1n1, v23_n10, v23_n11, v23_0n1, v23_00, v23_01, v23_1n1, v23_10, v23_11]})
        df24 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v24_n1n1, v24_n10, v24_n11, v24_0n1, v24_00, v24_01, v24_1n1, v24_10, v24_11]})
        df30 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v30_n1n1, v30_n10, v30_n11, v30_0n1, v30_00, v30_01, v30_1n1, v30_10, v30_11]})
        df31 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v31_n1n1, v31_n10, v31_n11, v31_0n1, v31_00, v31_01, v31_1n1, v31_10, v31_11]})
        df32 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v32_n1n1, v32_n10, v32_n11, v32_0n1, v32_00, v32_01, v32_1n1, v32_10, v32_11]})
        df33 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v33_n1n1, v33_n10, v33_n11, v33_0n1, v33_00, v33_01, v33_1n1, v33_10, v33_11]})
        df34 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v34_n1n1, v34_n10, v34_n11, v34_0n1, v34_00, v34_01, v34_1n1, v34_10, v34_11]})
        df40 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v40_n1n1, v40_n10, v40_n11, v40_0n1, v40_00, v40_01, v40_1n1, v40_10, v40_11]})
        df41 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v41_n1n1, v41_n10, v41_n11, v41_0n1, v41_00, v41_01, v41_1n1, v41_10, v41_11]})
        df42 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v42_n1n1, v42_n10, v42_n11, v42_0n1, v42_00, v42_01, v42_1n1, v42_10, v42_11]})
        df43 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v43_n1n1, v43_n10, v43_n11, v43_0n1, v43_00, v43_01, v43_1n1, v43_10, v43_11]})
        df44 = pd.DataFrame(
            {'X-direction': [-1, -1, -1, 0, 0, 0, 1, 1, 1], 'Y-direction': [-1, 0, 1, -1, 0, 1, -1, 0, 1],
             'test': ['value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:', 'value:'],
             'value': [v44_n1n1, v44_n10, v44_n11, v44_0n1, v44_00, v44_01, v44_1n1, v44_10, v44_11]})

        pivot00 = df00.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot01 = df01.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot02 = df02.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot03 = df03.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot04 = df04.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot10 = df10.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot11 = df11.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot12 = df12.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot13 = df13.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot14 = df14.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot20 = df20.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot21 = df21.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot22 = df22.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot23 = df23.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot24 = df24.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot30 = df30.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot31 = df31.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot32 = df32.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot33 = df33.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot34 = df34.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot40 = df40.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot41 = df41.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot42 = df42.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot43 = df43.pivot(index='X-direction', columns='Y-direction', values='value')
        pivot44 = df44.pivot(index='X-direction', columns='Y-direction', values='value')

        directory = str(model)
        parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results/test'
        path = os.path.join(parent_dir, directory)
        if not path:
            os.mkdir(path)

        fig, axn = plt.subplots(5, 5, sharex=True, sharey=True, figsize=(10, 10))

        for ax in axn.flat:
            ax.set_axis_off()
            im = ax.imshow(np.random.random((16, 16)), cmap='vlag', vmin=-1, vmax=1)

        cb_ax = fig.add_axes([.91, .3, .03, .4])
        cb_ax = fig.colorbar(im, cax=cb_ax)
        # cbar.set_ticks([])

        ax = plt.subplot(5, 5, 1)
        sns.heatmap(pivot00, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 2)
        sns.heatmap(pivot01, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 3)
        sns.heatmap(pivot02, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 4)
        sns.heatmap(pivot03, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 5)
        sns.heatmap(pivot04, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 6)
        sns.heatmap(pivot10, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 7)
        sns.heatmap(pivot11, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 8)
        sns.heatmap(pivot12, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 9)
        sns.heatmap(pivot13, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 10)
        sns.heatmap(pivot14, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 11)
        sns.heatmap(pivot20, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 12)
        sns.heatmap(pivot21, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 13)
        sns.heatmap(pivot22, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 14)
        sns.heatmap(pivot23, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 15)
        sns.heatmap(pivot24, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 16)
        sns.heatmap(pivot30, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 17)
        sns.heatmap(pivot31, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 18)
        sns.heatmap(pivot32, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 19)
        sns.heatmap(pivot33, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 20)
        sns.heatmap(pivot34, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 21)
        sns.heatmap(pivot40, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 22)
        sns.heatmap(pivot41, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 23)
        sns.heatmap(pivot42, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 24)
        sns.heatmap(pivot43, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        ax = plt.subplot(5, 5, 25)
        sns.heatmap(pivot44, annot=False, fmt="g", vmin=-1, vmax=1, cmap='vlag',  cbar=False, ax=ax)
        ax.set_aspect('equal')

        fig.tight_layout(rect=[0, 0, .9, 1])
        fig.savefig(path + '/' + str(model) + '_' + label + '_' +  reward_info_out[a][2] + "_testprob.jpg")
        plt.close()

    print("Model {} testing visualization: complete".format(model))
