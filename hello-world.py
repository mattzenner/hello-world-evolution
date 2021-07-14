'''
### A long way to say hello.
'''

import string
import random


def hamming_distance(string1, string2):
	dist_counter = 0
	for n in range(len(string1)):
		if string1[n] != string2[n]:
			dist_counter += 1
	return dist_counter


def evolve():
        count = 0
        while True:
            count += 1
            if count % 1000 == 0:
                print('Passes: ', count)
            temp = survivors  #reproduction
            for x in range(5):
                survivors.extend(temp)

            num = 0
            for org in survivors:
                temp = org[0]  #mutation
                temp = list(temp)
                for x in range(len(temp)):
                    if random.random() <= mutation_prob:
                        temp[x] = random.choice(charspace)
                temp = ''.join(temp)
                mutation_successes.append(temp != org[0])
                survivors[survivors.index(org)] = (temp, hamming_distance(temp, target))
                if org[1] > num:
                    num = org[1]

            while len(survivors) > 10:  #selection
                index, highest = 0, 0
                for org in survivors:
                    if org[1] > highest:
                        highest = org[1]
                        index = survivors.index(org)
                del survivors[index]

            for org in survivors:
                if org[1] == 0:
                        return org, survivors, count


charspace = list(string.printable)
orgs = []
target = "print('hello world')"
org_len = len(target)
mutation_prob = 0.05

for i in range(10):
    temp = ''
    for x in range(len(target)):
        temp += random.choice(charspace)
    orgs.append(temp)

scores = [(org, hamming_distance(org, target)) for org in orgs]
survivors = scores
mutation_successes = []
org, survivors, count = evolve()
print(org)

for org in survivors:
    if org[1] == 0:
		print(org)
        exec(org[0])

print('Passes: ', count)
