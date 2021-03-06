import matplotlib.pyplot as pyplot
import re

BINS_NUMBER = 100
BIN_SPAN = 20
LOWER_BOUND = 338398
UPPER_BOUND =  774436

delta = (UPPER_BOUND - LOWER_BOUND)/float(BINS_NUMBER)

with open('parsed/history.csv','rb') as tweet_file:
    tweet_times = []
    for line in tweet_file:
        match = re.search('(\d+),', line)
        if match:
            tweet_times.append(int(match.group(1)))


visual_tweets = []
for time in tweet_times:
    visual_tweets.append(time) # the exact matching bin shows up two times 
    for i in range(BIN_SPAN):
        visual_tweets.append(time + delta*i) # adding up 'decay' period for smoothness


fig, ax = pyplot.subplots()
n, bins, patches = pyplot.hist(visual_tweets, BINS_NUMBER, normed=1, facecolor = 'blue', alpha = 0.5)
ax.invert_xaxis()
pyplot.savefig('plots/freq_hist.png')
