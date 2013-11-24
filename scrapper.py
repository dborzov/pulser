'''
pulser/scrapper.py

The resultant jsons are dumped into a file at the ./output folder, under the 'until' parameter value as the filename.
'''

import simplejson
import TwitterAPI
import access_keys
import time


COUNT_PARAMETER = '100'
OUTPUT_FOLDER = 'json'

TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json'
TWITTER_USERNAME = 'PeterBorzov'

api = TwitterAPI.TwitterAPI(access_keys.CONSUMER_KEY, access_keys.CONSUMER_SECRET, access_keys.ACCESS_TOKEN_KEY, access_keys.ACCESS_TOKEN_SECRET)
output = open(OUTPUT_FOLDER+ '/total.jsons','w')

start_time = time.time(); exec_time = 0.
counter = 2
total_tweets = 0
id_cursor = False
while counter > 1 and exec_time < 300.:
    exec_time = time.time()-start_time
    time.sleep(1.)  # some courtesy pause before quiring an api
    if not id_cursor:
        r = api.request('search/tweets', {'q':'rubikloud','count':COUNT_PARAMETER})
    else:
        print 'Tweets so far: %d, last query: %d , id: %s' % (total_tweets, counter, id_cursor)
        r = api.request('search/tweets', {'q':'rubikloud','count':COUNT_PARAMETER, 'max_id':id_cursor})
    counter = 0
    for item in r.get_iterator():
        output.write(simplejson.dumps(item)+'\n')
        counter +=1
        id_cursor = item['id']
    total_tweets += counter

print 'Totally: %d' % total_tweets