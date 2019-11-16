from collections import Counter
import random

import numpy as np
import matplotlib.pyplot as plt
'''
Applies voting algorithm
and generates answer
'''

f1 = 'submission_98.txt'
f2 = 'submission_2_98.txt'
f3 = 'submission_98_22.txt'

files = [f1,f2,f3]

files = list(map(lambda x: open(x, 'r'), files))

lines = list(map(lambda x: x.readlines(), files))

voting = list(map(lambda x: list(map(lambda z: int(z.strip()), x)), lines))

voting = list(zip(*voting))

solutions = []

good_votes = []

conflicts = []

for i, t in enumerate(voting):
    votes = Counter(t)
    if len(votes.items()) == 1:
        #only one vote, they agree
        v = votes.most_common(1)[0][0]
        solutions.append(v)
        good_votes.append(v)
        continue
    max_votes = votes.most_common(1)[0][1]
    most_voted = list(filter(lambda z: z[1] == max_votes, votes.items()))
    if len(most_voted) == 1:
        # more than one vote but majority
        solutions.append(most_voted[0][0])
        good_votes.append(most_voted[0][0])
        continue
    #save the special cases for later
    solutions.append(most_voted) #save all of them
    conflicts.append(i) #and the conflict
    continue
N_DIGITS = 10
average_prob = 1/N_DIGITS
count_good_votes = Counter(good_votes)
total = sum(count_good_votes.values())
dict_prob = {k: v/total for k, v in count_good_votes.items()}
dict_prob_avg_min = min(map(lambda z: average_prob - z, dict_prob.values()))
dict_prob = {k: (average_prob - v) + abs(dict_prob_avg_min) + 1 for k, v in dict_prob.items()}

for i in conflicts:
    votes = list(map(lambda x: x[0], solutions[i])) #get the vote, not the count
    probs = list(map(lambda x: dict_prob[x], votes))
    choice = random.choices(votes, probs, k=1)[0]
    solutions[i] = choice

for sol in solutions[:-1]:
    print(sol)
    pass
print(solutions[-1], end='')
