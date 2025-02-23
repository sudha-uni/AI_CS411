import math
from collections import Counter, defaultdict
import numpy as np
from scipy.stats import chi2


# Function Definitions
def plurality_value(examples):
    counts = Counter(example['WillWait'] for example in examples)
    return counts.most_common(1)[0][0]


def entropy(examples):
    labels = [example['WillWait'] for example in examples]
    counts = Counter(labels)
    total = len(labels)
    return -sum((count / total) * math.log2(count / total) for count in counts.values() if count > 0)


def information_gain(attribute, examples):
    total_entropy = entropy(examples)
    values = set(example[attribute] for example in examples)
    total = len(examples)
    subset_entropy = 0.0
    for value in values:
        subset = [example for example in examples if example[attribute] == value]
        subset_entropy += (len(subset) / total) * entropy(subset)
    return total_entropy - subset_entropy


def learn_decision_tree(examples, attributes, parent_examples):
    if not examples:
        return plurality_value(parent_examples)
    elif all(example['WillWait'] == examples[0]['WillWait'] for example in examples):
        return examples[0]['WillWait']
    elif not attributes:
        return plurality_value(examples)
    else:
        A = max(attributes, key=lambda attr: information_gain(attr, examples))
        
        tree = {'attribute': A, 'branches': {}}
        values = set(example[A] for example in examples)
        
        for value in values:
            subset = [example for example in examples if example[A] == value]
            subtree = learn_decision_tree(subset, [attr for attr in attributes if attr != A], examples)
            tree['branches'][value] = subtree
        
        return tree


def chi_squared_prune(tree, examples, alpha=0.05):
    if isinstance(tree, str):
        return tree
    
    attribute = tree['attribute']
    branches = tree['branches']
    
    observed_counts = defaultdict(Counter)
    total_counts = Counter(example['WillWait'] for example in examples)
    
    for value, subtree in branches.items():
        subset = [example for example in examples if example[attribute] == value]
        label_counts = Counter(example['WillWait'] for example in subset)
        for label, count in label_counts.items():
            observed_counts[value][label] += count
    
    expected_counts = defaultdict(Counter)
    for value, subset_counts in observed_counts.items():
        subset_total = sum(subset_counts.values())
        for label in total_counts:
            expected_counts[value][label] = subset_total * (total_counts[label] / len(examples))
    
    chi_squared_stat = 0
    for value in observed_counts:
        for label in total_counts:
            observed = observed_counts[value][label]
            expected = expected_counts[value][label]
            if expected > 0:
                chi_squared_stat += ((observed - expected) ** 2) / expected
    
    degrees_of_freedom = len(observed_counts) - 1
    critical_value = chi2.ppf(1 - alpha, degrees_of_freedom)
    
    if chi_squared_stat < critical_value:
        return plurality_value(examples)
    else:
        for value, subtree in branches.items():
            subset = [example for example in examples if example[attribute] == value]
            branches[value] = chi_squared_prune(subtree, subset, alpha)
        return tree


attribute_names = ['Alt', 'Bar', 'Fri', 'Hun', 'Pat', 'Price', 'Rain', 'Res', 'Type', 'Est', 'WillWait']

data = """
Yes, No,  No,  Yes, Some, $$$, No,   Yes, French,  0-10,   Yes
Yes, No,  No,  Yes, Full, $,   No,   No,  Thai,    30-60,  No
No,  Yes, No,  No,  Some, $,   No,   No,  Burger,  0-10,   Yes
Yes, No,  Yes, Yes, Full, $,   No,   No,  Thai,    10-30,  Yes
Yes, No,  Yes, No,  Full, $$$, No,   Yes, French,  >60,    No
No,  Yes, No,  Yes, Some, $$,  Yes,  Yes, Italian, 0-10,   Yes
No,  Yes, No,  No,  None, $,   Yes,  No,  Burger,  0-10,   No
No,  No,  No,  Yes, Some, $$,  Yes,  Yes, Thai,    0-10,   Yes
No,  Yes, Yes, No,  Full, $,   Yes,  No,  Burger,  >60,    No
Yes, Yes, Yes, Yes, Full, $$$, No,   Yes, Italian, 10-30,  No
No,  No,  No,  No,  None, $,   No,   No,  Thai,    0-10,   No
Yes, Yes, Yes, Yes, Full, $,   No,   No,  Burger,  30-60,  Yes
"""

lines = data.strip().split("\n")
examples = [dict(zip(attribute_names, line.split(", "))) for line in lines]

attributes = attribute_names[:-1]
decision_tree = learn_decision_tree(examples, attributes, examples)
print("\nDecision Tree Before Pruning: ")
print(decision_tree)

pruned_tree = chi_squared_prune(decision_tree, examples, alpha=0.05)
print("\nDecision Tree After Pruning: ")
print(pruned_tree)
