import simplejson
import re
import datetime
import os

FOLDER_NAME = 'json'


def datestring2datetime(datestring):
  "Translater Twitter datastamp string into datatime.datetime-type object"
  Month2MON = {'Jan':1,'Feb':2,'Mar':3,'Apr':4, 'May':5, 'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11, 'Dec':12}
  match = re.search('(\w\w\w) (\w\w\w) (\d\d) (\d\d):(\d\d):(\d\d) \+0000 (\d\d\d\d)', tweet_dict['created_at'])
  day_of_week, month, day, hour, minute, second, year = match.group(1,2,3,4,5,6,7)
  tweet_time = datetime.datetime(int(year),Month2MON[month], int(day), int(hour), int(minute), int(second))
  return tweet_time

reference_time = datetime.datetime.now()
tweet_counter = 0
time_lower_bound, time_upper_bound = 0, 0

out_file = open('parsed/history.csv','wb')
for file_name in os.listdir(FOLDER_NAME):
    with open(FOLDER_NAME + '/' + file_name,'rb') as in_file:
        for line in in_file:
            tweet_dict = simplejson.loads(line)
            tweet_time = datestring2datetime(tweet_dict['created_at'])
            time_diff = reference_time - tweet_time
            if time_diff.total_seconds() > time_lower_bound:
                time_lower_bound = time_diff.total_seconds()
            if time_diff.total_seconds() < time_upper_bound or time_upper_bound==0:
                time_upper_bound = time_diff.total_seconds()
            out_file.write('%d, "%s" , "%s" \n' % (time_diff.total_seconds(),tweet_dict['created_at'].encode('utf-8'), tweet_dict['text'].encode('utf-8').replace('\n',' ')))
            tweet_counter += 1

with open('consts.py','wb') as log_file:
    log_file.write("TOTAL_NUMBER_OF_TWEETS = %d \n" % tweet_counter)
    log_file.write("LOWER_BOUND, UPPER_BOUND = %d , %d \n" % (time_upper_bound, time_lower_bound))



