import matplotlib.pyplot as pyplot
import re

BINS_NUMBER = 30


with open('parsed/history.csv','rb') as tweet_file:
    tweet_times = []
    for line in tweet_file:
        match = re.search('(\d+),', line)
        if match:
            tweet_times.append(-int(match.group(1)))

n, bins, patches = pyplot.hist(tweet_times, BINS_NUMBER, normed=1, facecolor = 'blue', alpha = 0.5)
pyplot.savefig('plots/freq_hist.png')
