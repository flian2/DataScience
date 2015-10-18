import sys
import json

def uni2utf8(uni_string):
    unicode_string = uni_string
    encoded_string = unicode_string.encode('utf-8')
    return encoded_string

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
        print uni2utf8(word), value


    # print 'number of lines', n

if __name__ == '__main__':
    main()
