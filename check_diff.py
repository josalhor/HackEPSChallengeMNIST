f1 = 'submission_98.txt'
f2 = 'submission_2_98.txt'
f3 = 'submission_98_22.txt'
original_75 = 'submission_original.txt'
solutions = 'submission.txt'

files = [
    f1,
    f2,
    f3,
    original_75
]

def return_votes(f_n):
    with open(f_n, 'r') as f:
        x = f.readlines()
        return list(map(lambda z: int(z.strip()), x))

voting = list(map(return_votes, files))

solutions = return_votes(solutions)

total_number_votes = len(voting[0])
for i, f_n in enumerate(files):
    votes = voting[i]
    zipped = zip(votes, solutions)
    n_votes_different = len(list(filter(lambda z: z[0] != z[1], zipped)))
    percent_different = (n_votes_different / total_number_votes) * 100
    print(f'Final submission is different to {f_n} by {percent_different:.4f}%')