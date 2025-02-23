The LEARN-DECISION-TREE algorithm is a recursive method for constructing a decision tree from a set of examples. It embodies the basic idea of decision tree learning, which is to split the dataset based on the most informative attributes, creating a tree structure that can predict the outcome of new examples.

Base Cases:
    If there are no examples left: Return the most common classification (output value) from the parent examples using PLURALITY-VALUE.
    If all examples in the current set have the same classification: Return that classification as a leaf node.
    If there are no attributes left to split on: Return the most common classification in the current set of examples using PLURALITY-VALUE.

Recursive Case:
    Select the attribute A that is most informative for splitting the data. This is determined by the IMPORTANCE function (e.g., using metrics like Information Gain or Gini Index).
    Create a new decision tree with A as the root node.
    For each possible value v of attribute A:
    Filter the examples to those where the value of A is v.
    Recursively build a subtree using the filtered examples, the remaining attributes (attributes − A), and the current examples as the parent examples.

Construct the Tree:
    Add branches to the current tree for each possible value of A, linking them to the corresponding subtree.
    Return the completed tree.

Information Gain: Used to select the attribute that minimizes entropy after the split.
Chi-squared Pruning: Statistically determines whether splitting adds significant predictive power.
Alpha Value: Controls the level of pruning; smaller alpha values retain more complex trees.

How to Run: 
    Unzip the folder.
    Check if there are any errors in the decision.py file.
    Open a new terminal, type in "python decision.py" and hit Enter.