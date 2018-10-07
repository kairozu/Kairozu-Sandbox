# did you also forget the word combination for your master 643DWD lock?
# maybe these words will jog your memory :| note: this honestly worked for me
#
# this generates all combinations of letters (both backward and forward)
# and screens them for being actual dictionary words

import itertools
import enchant

dictionary = enchant.Dict("en_us")
# replace the letters below with the ones on your lock
round1 = ['R', 'S', 'T', 'L', 'N', 'B', 'D', 'M', 'J', 'P']
round2 = ['E', 'I', 'O', 'U', 'Y', 'R', 'T', 'L', 'H', 'A']
round3 = ['D', 'E', 'O', 'R', 'S', 'T', 'L', 'N', 'A', 'C']
round4 = ['L', 'N', 'E', 'D', 'H', 'K', 'Y', 'R', 'S', 'T']

count = 0
countr = 0
for combination in itertools.product(round1, round2, round3, round4):
    word = ''.join(combination)
    if dictionary.check(word):
        count = count+1
        print(str(count) + ": " + word)

for combination in itertools.product(round4, round3, round2, round1):
    word = ''.join(combination)
    if dictionary.check(word):
        countr = countr+1
        print(str(countr) + ": " + word)
