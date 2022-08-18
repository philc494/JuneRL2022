
import c1_8tablespos
import c1_8tablespos_probdist


def model_selector(model_no, parameters):
    if model_no == 1:
        return c1_8tablespos_probdist.qtables_8(parameters['train_pattern'], parameters['train_iterations'])
    if model_no == 2:
        return c1_8tablespos.qtables_8(parameters['train_pattern'], parameters['train_iterations'])


