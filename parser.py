import simplejson
import re

out_file = open('parsed/history.csv','wb')
with open('output/2013-11-19.jsons','rb') as in_file:
    for line in in_file:
        tweet_dict = simplejson.loads(line)
        match = re.search('(\w\w\w) (\w\w\w) (\d\d) (\d\d):\d\d:\d\d \+0000 (\d\d\d\d)',
         tweet_dict['created_at'])
        if match:
            day_of_week, month, day, hour, year = match.group(1), match.group(2), match.group(3), match.group(4), match.group(4)
            stringus = day + hour + ',"' + tweet_dict['text'] +'"\n'
            out_file.write(stringus.encode('utf8'))

# hour+u',"' + tweet_dict['text'].encode('utf8') +u'"'




