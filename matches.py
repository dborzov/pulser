# The script uses Twitter API to search for tweets mentioning rubikloud.
# The resultant jsons are dumped into a file at the ./output folder, under the 'until' parameter value as the filename.



import simplejson
import TwitterAPI
from access_keys import *

UNTIL_PARAMETER = '2013-11-20'
COUNT_PARAMETER = '100'

TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json'
TWITTER_USERNAME = 'PeterBorzov'



api = TwitterAPI.TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
r = api.request('search/tweets', {'q':'rubikloud', 'until':UNTIL_PARAMETER,'count':COUNT_PARAMETER})

output = open('output/'+UNTIL_PARAMETER+'.jsons','w')
for item in r.get_iterator():
    output.write(simplejson.dumps(item)+'\n')