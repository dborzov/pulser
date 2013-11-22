import simplejson
import re
import datetime
import pickle

def datestring2datetime(datestring):
  "Translater Twitter datastamp string into datatime.datetime-type object"
  Month2MON = {'Jan':1,'Feb':2,'Mar':3,'Apr':4, 'May':5, 'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11, 'Dec':12}
  match = re.search('(\w\w\w) (\w\w\w) (\d\d) (\d\d):(\d\d):(\d\d) \+0000 (\d\d\d\d)', tweet_dict['created_at'])
  day_of_week, month, day, hour, minute, second, year = match.group(1,2,3,4,5,6,7)
  tweet_time = datetime.datetime(int(year),Month2MON[month], int(day), int(hour), int(minute), int(second))
  return tweet_time


out_file = open('parsed/history.csv','wb')
with open('output/2013-11-19.jsons','rb') as in_file:
    for line in in_file:
        tweet_dict = simplejson.loads(line)
        tweet_time = datestring2datetime(tweet_dict['created_at'])
        in_file.write('%d:%d:%d \n' % (tweet_time.hour, tweet_time.minute, tweet_time.second))

# hour+u',"' + tweet_dict['text'].encode('utf8') +u'"'