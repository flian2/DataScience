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
            if encoded.get(u'entities'):
                if encoded.get(u'entities').get(u'hashtags'):
                    tags = encoded.get(u'entities').get(u'hashtags')
                    for tag in tags:
                        # print tag[u'text']
                        freq[tag[u'text']] = freq.get(tag[u'text'],0) + 1
                # for tag in tags:
                #     freq[tag] = freq.get(tag,0) + 1

    sorted_words = sorted(freq.keys(), key = freq.get, reverse = True)
    n = 1
    for word in sorted_words:
        if n > 10:
            break
        print uni2utf8(word), freq[word]
        n += 1


    # print 'number of lines', n

if __name__ == '__main__':
    main()
