import b_modelselector
import z_statistics
import a_tester
from z_visualization import visualize_tables
from z_testvisualization import visualize_testtables
from collections import defaultdict
import pandas as pd
import os
import time

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

cust1 = 'ABACAD' * 8
cust2 = 'AAAAAB' * 8
cust3 = 'ABAAAAAAAAAAAAABAAAAAAAA' * 2
cust4 = 'ABCDABCDABCDAAAA' * 3
cust5 = 'ABCDDCBA' * 6
cust6 = 'ABAC' * 12

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Models:
1/3: action-distribution, positive rewards
2/4: epsilon-greedy, positive rewards
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Select training criteria, models, and desired reports
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Models to analyze
model_list = [2]
seq_list = [seq1, seq3, seq7, cust1, cust2, cust3, cust4, cust5, cust6]
# seq_list = [seq1, seq3]

seq_labels = {seq1: 'seq1', seq3: 'seq3', seq4: 'seq4', seq7: 'seq7', cust1: 'cust1', cust2: 'cust2', cust3: 'cust3', cust4: 'cust4',
          cust5: 'cust5', cust6: 'cust6', seq10: 'seq10'}

# Parameters to be used, if applicable for given model(s)
# alpha_list = [.05, .25, .50]
alpha_list = [.25]
alpha_labels = {.05: '05', .25: '25', .5: '50'}

explore_list = [.05, .25, .50]
explore_labels = {.05: '05', .25: '25', .5: '50'}
exploration_rate = 0.2
exploration_label = '20'

# exp_list = [-.25, -.75, -1.25]
exp_list = [-.75]
exp_labels = {-.25: '25', -.75: '75', -1.25: '125'}

for seq in seq_list:
    for alpha in alpha_list:
        for exp_val in exp_list:
            # Patterns to analyze
            train_pattern = seq
            pattern_text = str(seq)
            train_iterations = 2000
            train_sets = 50
            test_iterations = 100000

            make_general_matrix = False
            statistics = True
            train_visualizations = True
            test_visualizations = True

            label = 'test_' + seq_labels[seq] + '_' + alpha_labels[alpha] + '_' + exp_labels[exp_val] + '_' \
                    + exploration_label

            """""""""""""""""""""""""""""""""""""""""""""""""""""""""""
            Run program
            """""""""""""""""""""""""""""""""""""""""""""""""""""""""""

            "Make transition matrix for train pattern"
            summaryinfo = {}
            test_pattern = train_pattern

            pattern_string = " ".join(train_pattern)
            result_1 = pattern_string.split(" ")
            n = 2  # grouping size
            m = 1  # overlap size
            string_pairs = [result_1[i:i + n] for i in range(0, len(result_1) - 1, n - m)]

            pair_list = []
            for string_pair in string_pairs:
                pair_list.append("".join(string_pair))

            AA_count = pair_list.count('AA')
            AB_count = pair_list.count('AB')
            AC_count = pair_list.count('AC')
            AD_count = pair_list.count('AD')
            BA_count = pair_list.count('BA')
            BB_count = pair_list.count('BB')
            BC_count = pair_list.count('BC')
            BD_count = pair_list.count('BD')
            CA_count = pair_list.count('CA')
            CB_count = pair_list.count('CB')
            CC_count = pair_list.count('CC')
            CD_count = pair_list.count('CD')
            DA_count = pair_list.count('DA')
            DB_count = pair_list.count('DB')
            DC_count = pair_list.count('DC')
            DD_count = pair_list.count('DD')

            try:
                AA_prob = AA_count / (AA_count + AB_count + AC_count + AD_count)
            except ZeroDivisionError:
                AA_prob = 0
            try:
                AB_prob = AB_count / (AA_count + AB_count + AC_count + AD_count)
            except ZeroDivisionError:
                AB_prob = 0
            try:
                AC_prob = AC_count / (AA_count + AB_count + AC_count + AD_count)
            except ZeroDivisionError:
                AC_prob = 0
            try:
                AD_prob = AD_count / (AA_count + AB_count + AC_count + AD_count)
            except ZeroDivisionError:
                AD_prob = 0
            try:
                BA_prob = BA_count / (BA_count + BB_count + BC_count + BD_count)
            except ZeroDivisionError:
                BA_prob = 0
            try:
                BB_prob = BB_count / (BA_count + BB_count + BC_count + BD_count)
            except ZeroDivisionError:
                BB_prob = 0
            try:
                BC_prob = BC_count / (BA_count + BB_count + BC_count + BD_count)
            except ZeroDivisionError:
                BC_prob = 0
            try:
                BD_prob = BD_count / (BA_count + BB_count + BC_count + BD_count)
            except ZeroDivisionError:
                BD_prob = 0
            try:
                CA_prob = CA_count / (CA_count + CB_count + CC_count + CD_count)
            except ZeroDivisionError:
                CA_prob = 0
            try:
                CB_prob = CB_count / (CA_count + CB_count + CC_count + CD_count)
            except ZeroDivisionError:
                CB_prob = 0
            try:
                CC_prob = CC_count / (CA_count + CB_count + CC_count + CD_count)
            except ZeroDivisionError:
                CC_prob = 0
            try:
                CD_prob = CD_count / (CA_count + CB_count + CC_count + CD_count)
            except ZeroDivisionError:
                CD_prob = 0
            try:
                DA_prob = DA_count / (DA_count + DB_count + DC_count + DD_count)
            except ZeroDivisionError:
                DA_prob = 0
            try:
                DB_prob = DB_count / (DA_count + DB_count + DC_count + DD_count)
            except ZeroDivisionError:
                DB_prob = 0
            try:
                DC_prob = DC_count / (DA_count + DB_count + DC_count + DD_count)
            except ZeroDivisionError:
                DC_prob = 0
            try:
                DD_prob = DD_count / (DA_count + DB_count + DC_count + DD_count)
            except ZeroDivisionError:
                DD_prob = 0

            transition_matrix = {'AA': AA_count, 'AB': AB_count, 'AC': AC_count, 'AD': AD_count, 'BA': BA_count,
                                 'BB': BB_count, 'BC': BC_count, 'BD': BD_count, 'CA': CA_count, 'CB': CB_count,
                                 'CC': CC_count, 'CD': CD_count, 'DA': DA_count, 'DB': DB_count, 'DC': DC_count,
                                 'DD': DD_count}

            transition_list = [(AA_count, AB_count, AC_count, AD_count), (BA_count, BB_count, BC_count, BD_count),
                               (CA_count, CB_count, CC_count, CD_count), (DA_count, DB_count, DC_count, DD_count)]

            df_transition = pd.DataFrame(transition_list, columns=['A', 'B', 'C', 'D'], index=['A', 'B', 'C', 'D'])

            transition_prob = [(AA_prob, AB_prob, AC_prob, AD_prob), (BA_prob, BB_prob, BC_prob, BD_prob),
                               (CA_prob, CB_prob, CC_prob, CD_prob), (DA_prob, DB_prob, DC_prob, DD_count)]

            df_prob = pd.DataFrame(transition_prob, columns=['A', 'B', 'C', 'D'], index=['A', 'B', 'C', 'D'])

            seq_preview = train_pattern[0:5]
            date_string = time.strftime("%Y%m%d %H.%M")
            directory = 'general'
            parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results/'
            path = os.path.join(parent_dir, directory)

            if make_general_matrix:
                writer = pd.ExcelWriter(path + '/' + label + '_tmatrix_' + seq_preview + '_' + '.xlsx',
                                        engine='xlsxwriter')
                df_prob.to_excel(writer, sheet_name='prob_matrix')
                df_transition.to_excel(writer, sheet_name='trans_matrix')
                writer.save()

            for a in model_list:
                summaryinfo[a] = {}
                summaryinfo[a]['trainiter'] = train_iterations
                summaryinfo[a]['trainsets'] = train_sets
                if test_pattern == seq1:
                    summaryinfo[a]['sequence'] = 'Seq1'
                elif test_pattern == seq2:
                    summaryinfo[a]['sequence'] = 'Seq2'
                elif test_pattern == seq3:
                    summaryinfo[a]['sequence'] = 'Seq3'
                elif test_pattern == seq4:
                    summaryinfo[a]['sequence'] = 'Seq4'
                elif test_pattern == seq5:
                    summaryinfo[a]['sequence'] = 'Seq5'
                elif test_pattern == seq6:
                    summaryinfo[a]['sequence'] = 'Seq6'
                elif test_pattern == seq7:
                    summaryinfo[a]['sequence'] = 'Seq7'
                elif test_pattern == seq8:
                    summaryinfo[a]['sequence'] = 'Seq8'
                elif test_pattern == seq9:
                    summaryinfo[a]['sequence'] = 'Seq9'
                elif test_pattern == seq10:
                    summaryinfo[a]['sequence'] = 'Seq10'
                elif test_pattern == seq11:
                    summaryinfo[a]['sequence'] = 'Seq11'
                else:
                    summaryinfo[a]['sequence'] = 'Custom'

                if a == 1:
                    summaryinfo[1]['description'] = '1: action-distribution, positive rewards'
                if a == 2:
                    summaryinfo[2]['description'] = '2: epsilon-greedy, positive rewards'

            parameters = {'train_pattern': train_pattern, 'test_pattern': test_pattern,
                          'train_iterations': train_iterations,
                          'test_iterations': test_iterations, "alpha": alpha, "exp_rate": exploration_rate,
                          "ExpVal": exp_val}

            # (input(" ---Train/Test Settings--- \n "
            #        "Pattern: {}\n Training iterations: {}\n Training sets: {}\n Test iterations: {}\n Label: {}\n"
            #        "---Press enter to continue--- ".format(train_pattern, train_iterations,
            #                                                train_sets, test_iterations, label
            #                                                )))
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
                    # print("Model {}, {}, alpha: {}, expval: {}, exprate: {}, training set {} completed"
                    #       .format(model, label, alpha, exp_val, exploration_rate, train_sets_done + 1))
                    train_sets_done += 1
                print("Model {}, {}, alpha: {}, expval: {}, exprate: {},  {} training sets completed"
                      .format(model, label, alpha, exp_val, exploration_rate, train_sets_done))

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

            for model in model_list:
                for b in table_list:
                    for c in pos_list:
                        for d in act_list:
                            resultsfinal[model][b][c][d] = round(sum(reward_tempdic[model][b][c][d].values()) / len(set_list), 2)

                test_results = a_tester.test_model(resultsfinal[model], test_sequence, model, parameters)
                if statistics:
                    z_statistics.stats(model, test_results, pattern_text, test_pattern, summaryinfo[model], label, alpha,
                                       exploration_rate, exp_val,
                                       test_iterations, train_iterations, train_sets)
                if train_visualizations:
                    visualize_tables(model, resultsfinal[model], label)
                AA_count = test_results['AAtrans']
                AB_count = test_results['ABtrans']
                AC_count = test_results['ACtrans']
                AD_count = test_results['ADtrans']
                Amid_count = test_results['Amidtrans']
                Aleft_count = test_results['Alefttrans']
                Aup_count = test_results['Auptrans']
                Adown_count = test_results['Adowntrans']
                Aright_count = test_results['Arighttrans']

                BA_count = test_results['BAtrans']
                BB_count = test_results['BBtrans']
                BC_count = test_results['BCtrans']
                BD_count = test_results['BDtrans']
                Bmid_count = test_results['Bmidtrans']
                Bleft_count = test_results['Blefttrans']
                Bup_count = test_results['Buptrans']
                Bdown_count = test_results['Bdowntrans']
                Bright_count = test_results['Brighttrans']

                CA_count = test_results['CAtrans']
                CB_count = test_results['CBtrans']
                CC_count = test_results['CCtrans']
                CD_count = test_results['CDtrans']
                Cmid_count = test_results['Cmidtrans']
                Cleft_count = test_results['Clefttrans']
                Cup_count = test_results['Cuptrans']
                Cdown_count = test_results['Cdowntrans']
                Cright_count = test_results['Crighttrans']

                DA_count = test_results['DAtrans']
                DB_count = test_results['DBtrans']
                DC_count = test_results['DCtrans']
                DD_count = test_results['DDtrans']
                Dmid_count = test_results['Dmidtrans']
                Dleft_count = test_results['Dlefttrans']
                Dup_count = test_results['Duptrans']
                Ddown_count = test_results['Ddowntrans']
                Dright_count = test_results['Drighttrans']

                transition_matrix = {'AA': AA_count, 'AB': AB_count,
                                     'AC': AC_count, 'AD': AD_count,
                                     'Amid': Amid_count, 'Aleft': Aleft_count,
                                     'Aright': Aright_count, 'Aup': Aup_count,
                                     'Adown': Adown_count,

                                     'BA': BA_count, 'BB': BB_count,
                                     'BC': BC_count, 'BD': BD_count,
                                     'Bmid': Bmid_count, 'Bleft': Bleft_count,
                                     'Bright': Bright_count, 'Bup': Bup_count,
                                     'Bdown': Bdown_count,

                                     'CA': CA_count, 'CB': CB_count,
                                     'CC': CC_count, 'CD': CD_count,
                                     'Cmid': Cmid_count, 'Cleft': Cleft_count,
                                     'Cright': Cright_count, 'Cup': Cup_count,
                                     'Cdown': Cdown_count,

                                     'DA': DA_count, 'DB': DB_count,
                                     'DC': DC_count, 'DD': DD_count,
                                     'Dmid': Dmid_count, 'Dleft': Dleft_count,
                                     'Dright': Dright_count, 'Dup': Dup_count,
                                     'Ddown': Ddown_count}

                transition_list = [(AA_count, AB_count, AC_count, AD_count, Amid_count, Aup_count, Adown_count,
                                    Aleft_count, Aright_count),
                                   (BA_count, BB_count, BC_count, BD_count, Bmid_count, Bup_count, Bdown_count,
                                    Bleft_count, Bright_count),
                                   (CA_count, CB_count, CC_count, CD_count, Cmid_count, Cup_count, Cdown_count,
                                    Cleft_count, Cright_count), (DA_count, DB_count, DC_count, DD_count,
                                                                 Dmid_count, Dup_count, Ddown_count,
                                                                 Dleft_count, Dright_count)]

                df_transition = pd.DataFrame(transition_list,
                                             columns=['A', 'B', 'C', 'D', 'Mid', 'Up', 'Down', 'Left', 'Right'],
                                             index=['A', 'B', 'C', 'D'])

                try:
                    AA_prob = AA_count / (AA_count + AB_count + AC_count + AD_count + Amid_count + Aleft_count
                                          + Aright_count + Aup_count + Adown_count)
                except ZeroDivisionError:
                    AA_prob = 0
                try:
                    AB_prob = AB_count / (AA_count + AB_count + AC_count + AD_count + Amid_count + Aleft_count
                                          + Aright_count + Aup_count + Adown_count)
                except ZeroDivisionError:
                    AB_prob = 0
                try:
                    AC_prob = AC_count / (AA_count + AB_count + AC_count + AD_count + Amid_count + Aleft_count
                                          + Aright_count + Aup_count + Adown_count)
                except ZeroDivisionError:
                    AC_prob = 0
                try:
                    AD_prob = AD_count / (AA_count + AB_count + AC_count + AD_count + Amid_count + Aleft_count
                                          + Aright_count + Aup_count + Adown_count)
                except ZeroDivisionError:
                    AD_prob = 0
                try:
                    Amid_prob = Amid_count / (AA_count + AB_count + AC_count + AD_count + Amid_count + Aleft_count
                                              + Aright_count + Aup_count + Adown_count)
                except ZeroDivisionError:
                    Amid_prob = 0
                try:
                    Aleft_prob = Aleft_count / (AA_count + AB_count + AC_count + AD_count + Amid_count + Aleft_count
                                                + Aright_count + Aup_count + Adown_count)
                except ZeroDivisionError:
                    Aleft_prob = 0
                try:
                    Aup_prob = Aup_count / (AA_count + AB_count + AC_count + AD_count + Amid_count + Aleft_count
                                            + Aright_count + Aup_count + Adown_count)
                except ZeroDivisionError:
                    Aup_prob = 0
                try:
                    Adown_prob = Adown_count / (AA_count + AB_count + AC_count + AD_count + Amid_count + Aleft_count
                                                + Aright_count + Aup_count + Adown_count)
                except ZeroDivisionError:
                    Adown_prob = 0
                try:
                    Aright_prob = Aright_count / (AA_count + AB_count + AC_count + AD_count + Amid_count + Aleft_count
                                                  + Aright_count + Aup_count + Adown_count)
                except ZeroDivisionError:
                    Aright_prob = 0

                try:
                    BA_prob = BA_count / (BA_count + BB_count + BC_count + BD_count + Bmid_count + Bleft_count
                                          + Bright_count + Bup_count + Bdown_count)
                except ZeroDivisionError:
                    BA_prob = 0
                try:
                    BB_prob = BB_count / (BA_count + BB_count + BC_count + BD_count + Bmid_count + Bleft_count
                                          + Bright_count + Bup_count + Bdown_count)
                except ZeroDivisionError:
                    BB_prob = 0
                try:
                    BC_prob = BC_count / (BA_count + BB_count + BC_count + BD_count + Bmid_count + Bleft_count
                                          + Bright_count + Bup_count + Bdown_count)
                except ZeroDivisionError:
                    BC_prob = 0
                try:
                    BD_prob = BD_count / (BA_count + BB_count + BC_count + BD_count + Bmid_count + Bleft_count
                                          + Bright_count + Bup_count + Bdown_count)
                except ZeroDivisionError:
                    BD_prob = 0
                try:
                    Bmid_prob = Bmid_count / (BA_count + BB_count + BC_count + BD_count + Bmid_count + Bleft_count
                                              + Bright_count + Bup_count + Bdown_count)
                except ZeroDivisionError:
                    Bmid_prob = 0
                try:
                    Bleft_prob = Bleft_count / (BA_count + BB_count + BC_count + BD_count + Bmid_count + Bleft_count
                                                + Bright_count + Bup_count + Bdown_count)
                except ZeroDivisionError:
                    Bleft_prob = 0
                try:
                    Bup_prob = Bup_count / (BA_count + BB_count + BC_count + BD_count + Bmid_count + Bleft_count
                                            + Bright_count + Bup_count + Bdown_count)
                except ZeroDivisionError:
                    Bup_prob = 0
                try:
                    Bdown_prob = Bdown_count / (BA_count + BB_count + BC_count + BD_count + Bmid_count + Bleft_count
                                                + Bright_count + Bup_count + Bdown_count)
                except ZeroDivisionError:
                    Bdown_prob = 0
                try:
                    Bright_prob = Bright_count / (BA_count + BB_count + BC_count + BD_count + Bmid_count + Bleft_count
                                                  + Bright_count + Bup_count + Bdown_count)
                except ZeroDivisionError:
                    Bright_prob = 0

                try:
                    CA_prob = CA_count / (CA_count + CB_count + CC_count + CD_count + Cmid_count + Cleft_count
                                          + Cright_count + Cup_count + Cdown_count)
                except ZeroDivisionError:
                    CA_prob = 0
                try:
                    CB_prob = CB_count / (CA_count + CB_count + CC_count + CD_count + Cmid_count + Cleft_count
                                          + Cright_count + Cup_count + Cdown_count)
                except ZeroDivisionError:
                    CB_prob = 0
                try:
                    CC_prob = CC_count / (CA_count + CB_count + CC_count + CD_count + Cmid_count + Cleft_count
                                          + Cright_count + Cup_count + Cdown_count)
                except ZeroDivisionError:
                    CC_prob = 0
                try:
                    CD_prob = CD_count / (CA_count + CB_count + CC_count + CD_count + Cmid_count + Cleft_count
                                          + Cright_count + Cup_count + Cdown_count)
                except ZeroDivisionError:
                    CD_prob = 0
                try:
                    Cmid_prob = Cmid_count / (CA_count + CB_count + CC_count + CD_count + Cmid_count + Cleft_count
                                              + Cright_count + Cup_count + Cdown_count)
                except ZeroDivisionError:
                    Cmid_prob = 0
                try:
                    Cleft_prob = Cleft_count / (CA_count + CB_count + CC_count + CD_count + Cmid_count + Cleft_count
                                                + Cright_count + Cup_count + Cdown_count)
                except ZeroDivisionError:
                    Cleft_prob = 0
                try:
                    Cup_prob = Cup_count / (CA_count + CB_count + CC_count + CD_count + Cmid_count + Cleft_count
                                            + Cright_count + Cup_count + Cdown_count)
                except ZeroDivisionError:
                    Cup_prob = 0
                try:
                    Cdown_prob = Cdown_count / (CA_count + CB_count + CC_count + CD_count + Cmid_count + Cleft_count
                                                + Cright_count + Cup_count + Cdown_count)
                except ZeroDivisionError:
                    Cdown_prob = 0
                try:
                    Cright_prob = Cright_count / (CA_count + CB_count + CC_count + CD_count + Cmid_count + Cleft_count
                                                  + Cright_count + Cup_count + Cdown_count)
                except ZeroDivisionError:
                    Cright_prob = 0

                try:
                    DA_prob = DA_count / (DA_count + DB_count + DC_count + DD_count + Dmid_count + Dleft_count
                                          + Dright_count + Dup_count + Ddown_count)
                except ZeroDivisionError:
                    DA_prob = 0
                try:
                    DB_prob = DB_count / (DA_count + DB_count + DC_count + DD_count + Dmid_count + Dleft_count
                                          + Dright_count + Dup_count + Ddown_count)
                except ZeroDivisionError:
                    DB_prob = 0
                try:
                    DC_prob = DC_count / (DA_count + DB_count + DC_count + DD_count + Dmid_count + Dleft_count
                                          + Dright_count + Dup_count + Ddown_count)
                except ZeroDivisionError:
                    DC_prob = 0
                try:
                    DD_prob = DD_count / (DA_count + DB_count + DC_count + DD_count + Dmid_count + Dleft_count
                                          + Dright_count + Dup_count + Ddown_count)
                except ZeroDivisionError:
                    DD_prob = 0
                try:
                    Dmid_prob = Dmid_count / (DA_count + DB_count + DC_count + DD_count + Dmid_count + Dleft_count
                                              + Dright_count + Dup_count + Ddown_count)
                except ZeroDivisionError:
                    Dmid_prob = 0
                try:
                    Dleft_prob = Dleft_count / (DA_count + DB_count + DC_count + DD_count + Dmid_count + Dleft_count
                                                + Dright_count + Dup_count + Ddown_count)
                except ZeroDivisionError:
                    Dleft_prob = 0
                try:
                    Dup_prob = Dup_count / (DA_count + DB_count + DC_count + DD_count + Dmid_count + Dleft_count
                                            + Dright_count + Dup_count + Ddown_count)
                except ZeroDivisionError:
                    Dup_prob = 0
                try:
                    Ddown_prob = Ddown_count / (DA_count + DB_count + DC_count + DD_count + Dmid_count + Dleft_count
                                                + Dright_count + Dup_count + Ddown_count)
                except ZeroDivisionError:
                    Ddown_prob = 0
                try:
                    Dright_prob = Dright_count / (DA_count + DB_count + DC_count + DD_count + Dmid_count + Dleft_count
                                                  + Dright_count + Dup_count + Ddown_count)
                except ZeroDivisionError:
                    Dright_prob = 0

                transition_prob = [(AA_prob, AB_prob, AC_prob, AD_prob, Amid_prob, Aup_prob, Adown_prob,
                                    Aleft_prob, Aright_prob),
                                   (BA_prob, BB_prob, BC_prob, BD_prob, Bmid_prob, Bup_prob, Bdown_prob,
                                    Bleft_prob, Bright_prob),
                                   (CA_prob, CB_prob, CC_prob, CD_prob, Cmid_prob, Cup_prob, Cdown_prob,
                                    Cleft_prob, Cright_prob), (DA_prob, DB_prob, DC_prob, DD_prob,
                                                               Dmid_prob, Dup_prob, Ddown_prob,
                                                               Dleft_prob, Dright_prob)]

                df_prob = pd.DataFrame(transition_prob, columns=['A', 'B', 'C', 'D', 'Mid', 'Up', 'Down', 'Left', 'Right'],
                                       index=['A', 'B', 'C', 'D'])

                seq_preview = train_pattern[0:8]
                date_string = time.strftime("%Y%m%d %H.%M")
                directory = str(model)
                parent_dir = '/Users/philcrawford/PycharmProjects/JuneRL2022/results/test/'
                path = os.path.join(parent_dir, directory)

                writer = pd.ExcelWriter(path + '/' + str(model) + '_' + label + '_' + 'tmatrix_' + seq_preview + '.xlsx',
                                        engine='xlsxwriter')
                df_prob.to_excel(writer, sheet_name='prob_matrix')
                df_transition.to_excel(writer, sheet_name='trans_matrix')
                writer.save()

                board_rows = 5
                board_cols = 5

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
                if test_visualizations:
                    visualize_testtables(model, metatestdic, label)

