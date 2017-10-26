#!/usr/bin/python

import sys
# Collect the sum of scores for each state
totalScore = 0
oldState = None
# Gather the scores for the same key, then the key will change and we'll gather scores for the next state
for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# something is wrong, skip this line
		continue
	thisState, thisScore = data_mapped
	if thisState != oldState and oldState:
		print oldState, "\t", totalScore
		totalScore = 0 
	oldState = thisState
	totalScore += int(thisScore)

if oldState:
	print oldState, "\t", totalScore
