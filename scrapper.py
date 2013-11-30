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
TWITTER_GEOCODE = "49.25,-123.6,1000km" # Vancouver Metro Area and North Washington State
QUERY = 'tired today'

api = TwitterAPI.TwitterAPI(access_keys.CONSUMER_KEY, access_keys.CONSUMER_SECRET, access_keys.ACCESS_TOKEN_KEY, access_keys.ACCESS_TOKEN_SECRET)
output = open(OUTPUT_FOLDER+ '/total.jsons','w')

start_time = time.time(); exec_time = 0.
counter = 2
total_tweets = 0
id_cursor = False
while counter > 1 and exec_time < 300.:
    exec_time = time.time()-start_time
    time.sleep(1.)  # some courtesy pause before querying the api
    if not id_cursor:
        r = api.request('search/tweets', {'q':QUERY,'count':COUNT_PARAMETER,'geocode':TWITTER_GEOCODE})
    else:
        print 'Tweets so far: %d, last query: %d , id: %s , time in seconds: %d ' % (total_tweets, counter, id_cursor, exec_time)
        r = api.request('search/tweets', {'q':QUERY,'count':COUNT_PARAMETER, 'max_id':id_cursor, 'geocode':TWITTER_GEOCODE})
    counter = 0
    for item in r.get_iterator():
        output.write(simplejson.dumps(item)+'\n')
        counter +=1
        id_cursor = item['id']
    total_tweets += counter

if exec_time > 300.:
    print 'Stopping because of the Time limit.'

print 'Totally: %d' % total_tweets