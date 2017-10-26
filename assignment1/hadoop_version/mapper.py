#!/usr/bin/python
# for each tweet, extract the state info
# Build a dictionary state => score
# For each tweet, sum up scores to the dictionary key "state"
# Sort the dictionary according to values
import sys
import json

def read_cache():
    for line in open('afinn'):
	term, score = line.split('\t')
	scores[term] = int(score)

def uni2utf8(uni_string):
    unicode_string = uni_string
    encoded_string = unicode_string.encode('utf-8')
    return encoded_string

def tweet_sentiment(encoded, scores):
    # encoded: verified tweet in jason format
    # scores: the sentiment dictionary
    words = encoded[u'text'].split();
    sum_score = 0;
    for word in words:
        sum_score += scores.get(word,0)
    return sum_score

# put this into distributed cache later
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

scores = {} # dictionary of sentiment scores versus word
read_cache()
# read in twitter
# map: key: state, value: score
for line in sys.stdin:
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
                        print "{0}\t{1}".format(state, tweet_sentiment(encoded, scores))
        # 2. check user location
        elif encoded.get(u'user'):
            user = encoded.get(u'user')
            if user.get(u'location'):
                names = user.get(u'location').split(', ')
                for name in names:
                    if abv2states.get(name):
                        state = name;
                        print "{0}\t{1}".format(state, tweet_sentiment(encoded, scores))
