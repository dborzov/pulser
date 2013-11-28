import matplotlib.pyplot as pyplot
import re
from consts import *
import datetime

BINS_NUMBER = 100
BIN_SPAN = 20

delta = (UPPER_BOUND - LOWER_BOUND)/float(BINS_NUMBER)


def datestring2datetime(datestring):
  "Translater Twitter datastamp string into datatime.datetime-type object"
  Month2MON = {'Jan':1,'Feb':2,'Mar':3,'Apr':4, 'May':5, 'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11, 'Dec':12}
  match = re.search('(\w\w\w) (\w\w\w) (\d\d) (\d\d):(\d\d):(\d\d) \+0000 (\d\d\d\d)', datestring)
  day_of_week, month, day, hour, minute, second, year = match.group(1,2,3,4,5,6,7)
  tweet_time = datetime.datetime(int(year),Month2MON[month], int(day), int(hour), int(minute), int(second))
  return tweet_time


with open('parsed/history.csv','rb') as tweet_file:
    tweet_times = []
    labels = []
    for line in tweet_file:
        match = re.search('(\d+), "(\w\w\w \w\w\w \d\d \d\d:\d\d:\d\d \+0000 \d\d\d\d)"', line)
        if match:
            tweet_times.append(int(match.group(1)))
            tweet_time = datestring2datetime(match.group(2))
            labels.append('Nov ' + str(tweet_time.day))


visual_tweets = []
for time in tweet_times:
    visual_tweets.append(time) # the exact matching bin shows up two times
    for i in range(BIN_SPAN):
        visual_tweets.append(time + delta*i) # adding up 'decay' period for smoothness

nR, binsR, patchesR = pyplot.hist(tweet_times, BINS_NUMBER, facecolor = 'blue', alpha = 0.5)
n, bins, patches = pyplot.hist(visual_tweets, BINS_NUMBER, facecolor = 'blue', alpha = 0.5)

with open('frontend/js/data.js','wb') as js_file:
    js_string = '['
    index_string = '['
    for ii, column in enumerate(reversed(bins[:-1])):
        js_string += str(-column) + ', '
        index_string += str(ii) + ', '
    js_file.write('x_data = [' +index_string[:-2] + '],'+ js_string[:-2] + ']]; \n \n')

    js_string = ''
    for ii, column in enumerate(reversed(nR[:-1])):
        js_string += str(column) + ', '
    js_file.write('actually_data = [' +js_string[:-2] + ']; \n \n')


    js_string = '['
    for column in reversed(n):
        js_string += str(column) + ', '
    js_file.write('y_data = [' +index_string[:-2] + '],'+ js_string[:-2] + ']]; \n \n')
    js_string = ''

    for time in reversed(bins):
        i=0
        while(tweet_times[i]<time and i < len(tweet_times)):
            i += 1
        js_string += '"'+labels[i] + '", '
    js_file.write('data_labels = [' + js_string[:-2]+ ']; \n \n')


