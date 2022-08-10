import b_modelselector
import z_statistics
from z_visualization import visualize_tables

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
I. Select parameters
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
train_pattern = "ABC"
test_pattern = train_pattern
train_iterations = 50
test_iterations = 1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
II. Select models to analyze:
0: Orig backup
1: 8 Q-tables: negative reward possible
2: 8 Q-tablespos: game over at 50, no negative rewards
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
model_list = [2]


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
III. Run program
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

parameters = {'train_pattern': train_pattern, 'test_pattern': test_pattern, 'train_iterations': train_iterations,
              'test_iterations': test_iterations}

(input(" ---Train/Test Settings--- \n "
              "Training pattern: {}\n Iterations: {}\n Total training games: {}\n Testing pattern: {}\n Testing iterations: {}\n"
                " Total testing games: {}\n  "
              "---Press enter to continue--- ".format(train_pattern, train_iterations, len(train_pattern) * train_iterations,
                                                           test_pattern, test_iterations, len(test_pattern) * test_iterations,
                                                           )))
results = {}
stats = {}
for model in model_list:
    results[model] = b_modelselector.model_selector(model, parameters)
    # stats[model] = z_statistics.stats(model, results)
    # visualize_tables(model, results)




# todo:
    """
    Statistics/visualization to add:
    - plotting DFs from different models in same file for comparison
    - plotting epochs/etc from different models in same graph for comparison
    - plot all the parameters used to avoid confusion of which model was run
    other stats:
    - time to run
    - % of time int state leads directly to target
    - test: average moves per game 
    - train/test: ratio of avg test game length to avg train game length
    - test: average distance after int state to next target
    - test: average distance from middle after int state
    - test: average times per game wrong corner touched before right corner
    - 
    """
