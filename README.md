# HackEPSChallengeMNIST

Author: Josep Maria Salvia Hornos \
Solution file: `submission.txt`

## Overall proposed solution:

1. Generate a bigger and richer data-set
2. Generate 3 different neural networks with 3 convolutional layers and 3 dense layers
3. Apply a voting algorithm to decide on the conflicts between the neural networks
4. Apply uniform distribution probability and random selection on the conflicts of the voting algorithm
5. ??
6. Profit

## Steps

1. `generate_set.py` contains the code for set generation. We generate a data set with the same numbers but 8 different noise applications per image. This is KEY for the process to work, otherwise it may learn to associate a certain noise pattern to a certain drawing.
2. Train the neural network that is available at `submission_script_tensor.py` three times. With each neural network we get around 97.8-98.5% accuracy. We generate three files: `submission_2_98.txt`, `submission_98_22.txt` and `submission_98.txt`.
3. Validate the solution properly. I've left the files `testing.py` and `extra_info.py` that have helped me validate the solutions.
4. Apply the voting algorithm on `vote.py` and decide on the conflicts of the voting algorithm with an expected uniform distribution probability of the outcomes and weight them appropriately. We generate the file `submissions.txt`.
5. Validate the difference of the final submission (`submissions.txt`) vs the previous files and the original file available on the repo (`submission_original.txt` with an expected 75% accuracy). We do this with the file `check_diff.py`.

## Facts and notes

1. Expected final accuracy should be higher than 95% at minimum, expected over 97%.
2. Some numbers are impossible to decide because of the white patches, accuracy of over 99% is impossible.
3. Voting algorithms reduce conflicts overall by about 1.5%, probably increasing accuracy. That being said because of time constraints this was not tested against the test data-set.
4. Neural Networks take quite a long time to train, sometimes they don't even get fully trained.
5. Surprisingly there is a 30% between the proposed solution and the original submission file. That is weird, as one would expect only a 25% discrepancy coming from a classifier with 75% accuracy on the test data-set vs ours at around 98-99% accuracy. We attribute the discrepancy to randomness and overfitting.
6. Even though the original problem says that other metrics aside from accuracy will be taken into account that information is not useful for the problem at hand.
   1. Misclassification of numbers based on their similarity is a thing. One cannot expect that 5 and 6 are not confused less than 1 and 6 given the noise in the problem.
   2. There isn't a worse misclassification between categories. Misclassifying a 1 and a 7 should have the same weight as misclassifying a 9 and a 2 (for example). We are not dealing with a sick patient kind of situation where we have to consider the balance between false negatives and false positives (etc.)
   3. At around 98.5% accuracy we're almost at the ceiling of classification for this particular problem to the point where these other metrics don't really make sense without a misclassification weighting table.
7. For the organizers: Did you actually get a better classifier than I did?