import sys
import json

# Derive the sentiment of each tweet
# 1. Build dictionary for the list file
# 2. For each word in a tweet, if it's contained in the dictionary, sum up the sentiment scores
def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # lines(sent_file)
    # lines(tweet_file)

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
        # print line
        encoded = json.loads(line)
        if encoded.get(u'text'):
            # print encoded[u'text']
            # score
            words = encoded[u'text'].split();
            sum_score = 0;
            for word in words:
                if scores.get(word):
                    sum_score += scores[word]
            print sum_score
        n += 1
    

if __name__ == '__main__':
    main()
    # python tweet_sentiment.py AFINN-111.txt output.txt
