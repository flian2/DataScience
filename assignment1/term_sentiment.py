

import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # build dictionary for sent_file
    scores = {} # initialize an empty dictionary
    afinnfile = open(sys.argv[1])
    for line in afinnfile:
    	term, score = line.split('\t')
    	scores[term] = int(score)

    # read in twitter
    n = 0
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        encoded = json.loads(line)
        if encoded.get(u'text'):
            print '#', n
            # print encoded[u'text']
            # score
            words = encoded[u'text'].split();
            next = -1 # nearest word in scores to the right
            prev = -1 # nearest word in scores to the left
            for i in range(len(words)):
                if not scores.get(words[i]):
                    # find the nearest 2 words in afinnfile
                    if next < i and next > -1:
                        prev = next
                    next = i
                    while next < len(words):
                        if not scores.get(words[next]): 
                            next += 1
                        else:
                            break
                            # next points to nearest word in score
                    if next < len(words) and prev > -1: 
                        derived_score = (scores.get(words[next])+scores.get(words[prev]))/float(2)
                    elif next < len(words) and prev == -1:
                        derived_score = scores.get(words[next])
                    else:
                        derived_score = 0 # not found
                    print 'word derived: ', words[i], derived_score
                    if prev > -1 and prev < len(words):
                        print 'left neighbour: ', words[prev], scores.get(words[prev])
                    if next > -1 and next < len(words):
                        print 'right neighbour: ', words[next], scores.get(words[next])
            n += 1


        



if __name__ == '__main__':
    main()
