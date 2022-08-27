"""
Aug26:
Done:
    - change Main to include assigning parameters across all models to be used in train and test 
            (and mentioning in Test results xls what was used)
    - in testing model: if model =1, then use this; if model = 2, then use this
- make transition probabilities based on 1000 test count:
        - record in each of 1000 tests where int state ends up
        - calculate/return probabilities
- make a new transition matrix XLS for each model
- make it so int state starts in center, not from very last trial

todo:

    - make visualization - train and visualization - test (so one can turn off separately)
- make transition probabilities based on 1000 test count:
        - make a visualization of the area it went to (add +1 to entire region every time it went there)
            (cross arm up = purple, this one = blue)
        
        




- Run models exactly as it operates -- "% of time ends up in quadrant A, B, C, D" to evaluate how often it "guesses"
right (A = 2x2 topleft; middle center exactly special) - then "middle lines"
   (count all 1000 trials)
- interesting parameters
   - learning rate
   - reward functions
   - action picking functions

paper:
   - "evaluating fundamentals of reinforcement learning" 
   - "this model can't handle X property of sequences" 
    - think about how changing parameters might change model behavior
        - identify "core problems" and how changing parameters don't address this issue
        - values spanning large range of a parameter (reward highly -, 0, +) --> some optimum 'sweet spot' point
            - demonstrate making arguments
        - "will it be able to do do X thing?"
   - "here are other versions of models - these could work, this likely wouldn't" "background knowledge"
   - don't leave open logical gaps
   
   Not as interesting once sufficient
   - train/test sets & games --> just pick large enough (interested in long run converge)
   - 





Aug18:
- initialize all as .01 in prob dist
   - so many zeroes
   
- 4x4 transition matrix to evaluate scenarios




- changing reward function and action choice exponents etc.
- staying = bonus


- probability to add new Q-table
  - 



Questions:
  - reward function - email question and decreasing with step time exponentially, max steps?
  -
  
  
""""""""""""
Aug10
Done:
- finished "sets" approach
- built test module / proved it follows path correctly
- made it start with an interim B 
- made test module mostly open to any parameters
- made model 1 that uses distribution instead of epsilon-greedy - raise to power?





- ABAC --> variance of Q values chosen


- next steps:
    try sequences from paper
    come up with decent measures for model performance - variance, distance, action moves, time taken
       - finish distance in testing and other training model
       
        

""""""""""""""



""""""
Later:
- jitter all act-pos directions, compare

Since Aug10 meeting:
- fixed so it applies reward of 0 even if max steps reached

Since Jul28 meeting:
- problem of deterministic but getting on bad paths
    - done: change so if a square = 0, it can't go there because it's never gone there
    - done: make it so reward decreases approaching 0 and is always positive
    - done: add visualization of the "best path"
    - todo: solve theoretically handling "ABCD ABACAD" results and the "best path" for the test
        - "game1:
        - "game2:
        - "game3:..."
    - todo: solve theoretically handling when it gets in a loop due to a hardly chosen, but high reward square
        - taking 2nd best option the 2nd time around? but for first or last move or middle?
        
        
        
    

Jul28 meeting:
- Test set: 1 sample w/o exploration
- stats: visualize avg. number of times pos-act was taken --> action count

- next steps
    - one game, take pos-act count + distance metric from interim + act moves, reset, do again
    
other models:
    -model: "exploration" = 2nd best option instead of random
    
parameters:
- # games trained

My next steps:
- build this metric of pos-act count










Ideas:

Soon:

Python
  - streamline script/files so they stay together as discrete chunks

Results / visualization
  - Making an "epochs" training graph similar to deep learning
  - Making an Excel stats summary for each scenario
  - graph mean reward

Model
  - add a scaling down reward by time -- maximum steps per epsiode (and reward can't be negative)
  - penalty for trying to run into a wall or illegal move
  - adding discount factor (backprop) and next state lookup - Q[s, a] = Q[s, a] + alpha*(R + gamma*Max[Q(s’, A)] - Q[s, a])
  - adding non-deterministic factor


Later:
- Transformer model?

Email idea:
If we decide to use this maxQ term - every position on the 5x5 grid getting rewarded each game would have as part of the reward update function this term. And this term would tell it to look at all possible neighboring squares (i.e. possible next squares) to inform the value update.

So if the agent goes to the center square (2,2) and goes up to (1,2) at some point before reaching the target A, and we need to calculate the new Q value for (2,2)(-1,0),  then the MaxQ term would take the max of the Scenario A position-action values of each of the 8 squares surrounding (2,2).

Is this where order in backpropagation finally becomes important? Because the target square (0,

Don't forget:
- 5.6789 hack

"""








"""
Meeting notes Jul7

Open questions/discuss:
- learning rate addition
- "int rewards A" -- stay is not always the highest, because it bounces around 4 moves?
- Gathering stats before moving to deep learning? (# of interim stays, time to finish X runs, etc.) or not until later?
- discount factor vs. step cost?
- Resetting the position after each game?

- "Post-A interim" --> rewarded when whatever next scenario is -- current one lets it be "psychic"

Stats:
- time to learn
- how often least optimal paths learned
- how often incorrect behavior
- how well it learns patterns -
- easy to hard sequences -- seeing what impacts performance (cases like ABACAD, comparing models)
-

Adjusting models:
- (1 - learn rate) inclusion/exclusion - speed of learning vs. accuracy vs. different patterns
- discount factor vs. step cost (for ABAC, at what point does it stop in the middle from higher step cost)

Paper:
- "if people do it like this, this would imply __"

Next steps:
- todo: fix interim
- visualization / graphics
- build a test condition
- Other RL models solving similar problems
- DQN
"""""