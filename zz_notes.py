"""
Questions:
  - reward function - email question and decreasing with step time exponentially, max steps?
  -
"""





"""
Since Jul28 meeting:
- problem of deterministic but getting on bad paths
    - done: change so if a square = 0, it can't go there because it's never gone there
    - done: make it so reward decreases approaching 0 and is always positive
    - todo: solve theoretically handling "ABCD ABACAD" results and testwise
        - "game1:
        - "game2:
        - "game3:..."
    - todo: solve theoretically handling when it gets in a loop
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
"""