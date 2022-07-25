import c1_8tables
import c2_gamma8tables


def model_selector(model_no, parameters):
    if model_no == 1:
        return c1_8tables.qtables_8(parameters['train_pattern'], parameters['test_pattern'],
                                   parameters['train_iterations'], parameters['test_iterations'])
    if model_no == 2:
        return c2_gamma8tables.qtables_8gamma(parameters['train_pattern'], parameters['test_pattern'],
                                   parameters['train_iterations'], parameters['test_iterations'])


"""""""""""""""""""""
Each model should take parameters as input, return 1) reward tables, and 2) games and moves per game stats
"""""""""""""""""""""
