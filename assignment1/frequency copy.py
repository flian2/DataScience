import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():

    # build dictionary for fequency of term
    freq = {} # initialize an empty dictionary

    # read in twitter
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        # print line
        encoded = json.loads(line)
        if encoded.get(u'text'):
            # print encoded[u'text']
            # score
            words = encoded[u'text'].split();
            for word in words:
                freq[word] = freq.get(word,0) + 1

    sum = 0
    for word in freq.keys():
        sum += freq[word]
    
    for word in freq.keys():
        value = (float) (freq[word])/sum
        print word, value


    # print 'number of lines', n

if __name__ == '__main__':
    main()
