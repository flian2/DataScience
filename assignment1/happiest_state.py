import sys
import json

def uni2utf8(uni_string):
    unicode_string = uni_string
    encoded_string = unicode_string.encode('utf-8')
    return encoded_string

def lines(fp):
    print str(len(fp.readlines()))

def tweet_sentiment(encoded, scores):
    # encoded: verified tweet in jason format
    # scores: the sentiment dictionary
    words = encoded[u'text'].split();
    sum_score = 0;
    for word in words:
        sum_score += scores.get(word,0)
    return sum_score

def main():

    abv2states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # build dictionary for sent_file
    scores = {} # initialize an empty dictionary
    state_scores = {} # sum of scores of tweets for one state
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
        if encoded.get(u'text'): # is a tweet
            # identify states :
            # 1. check place
            if encoded.get(u'place'):
                place = encoded.get(u'place')
                if place.get(u'full_name'):
                    names = place.get(u'full_name').split(', ')
                    # print names
                    for name in names: 
                        if abv2states.get(name):
                            state = name;
                            # print state
                            state_scores[state] = state_scores.get(state,0) + tweet_sentiment(encoded, scores)
            # 2. check user location
            elif encoded.get(u'user'):
                user = encoded.get(u'user')
                if user.get(u'location'):
                    names = user.get(u'location').split(', ')
                    for name in names:
                        if abv2states.get(name):
                            state = name;
                            # print state
                            state_scores[state] = state_scores.get(state,0) + tweet_sentiment(encoded, scores)

    n += 1
    # print 'number of lines', n

    # print the top 2 states
    states_sorted = sorted(state_scores.keys(), key=state_scores.get, reverse=True)
    print states_sorted[0]

if __name__ == '__main__':
    main()
