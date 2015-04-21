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
    # print 'number of lines', n

if __name__ == '__main__':
    main()
