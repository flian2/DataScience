# derived score is decided by the neareast 2 word on the left and right
# that appears in the dictionary.

# Build a dictionary new_scores to store the derived (term, score)
# iterate each line of tweets to cummulate scores

# for each word in tweet, if it's not contained in old list, sum the derived score in the new list

import sys
import json


def lines(fp):
    print str(len(fp.readlines()))

def uni2utf8(uni_string):
    unicode_string = uni_string
    encoded_string = unicode_string.encode('utf-8')
    return encoded_string

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # build dictionary for sent_file
    scores = {} # initialize an empty dictionary
    new_scores = {}
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
            # print '#', n
            # print encoded[u'text']
            # score
            words = encoded[u'text'].split();
            next = -1 # nearest word in scores to the right
            prev = -1 # nearest word in scores to the left
            for i in range(len(words)):
                if not scores.get(words[i]):
                    new_word = words[i];
                    # find the nearest 2 words in afinnfile
                    next = i
                    while next < len(words):
                        if not scores.get(words[next]): 
                            next += 1
                        else:
                            break
                            # next points to nearest word in score
                    if next < len(words) and prev > -1: 
                        new_scores[new_word] = new_scores.get(new_word,0) + (scores.get(words[next])+scores.get(words[prev]))/float(2)
                    elif next < len(words) and prev == -1:
                        new_scores[new_word] = new_scores.get(new_word,0) + scores.get(words[next])
                else: # word in score
                    prev = i
            n += 1
    # print the new scores
    for word in new_scores:
        print uni2utf8(word), float(new_scores[word])


if __name__ == '__main__':
    main()
    # python term_sentiment.py AFINN-111.txt output.txt
