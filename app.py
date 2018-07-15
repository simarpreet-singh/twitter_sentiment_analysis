import tweepy
import csv

from textblob import TextBlob

consumer_key = 'hjnX0l1HObHveDvZBkdA8ZwMl'
consumer_secret = '5tKoNNSOdSkRbYjYfGTXG7OzhzbuzVmA0lUdiWB8jJ0lBmPkkk'

access_token = '1027502642-d9j0WSCQsC4CaSHpvcTLSqhqljrH7Q4Xev1NQ4Y'
access_token_secret = '55VuUhECrkTegGUy7jN7z9WMivrNbCdMyYZzVhSlo800p'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

searchWord = input('Enter a word to analyze from twitter: ')

public_tweets = api.search(searchWord)

# for tweet in public_tweets:
#     print(tweet.text)
#     analysis = TextBlob(tweet.text)
#     print(analysis.sentiment)



an_list = [ ]
tweet_list = [ ]
label = [ ]

with open(searchWord+'.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    for tweet in public_tweets:
        tweet_list.append(tweet.text)
        an_list.append(TextBlob(tweet.text).sentiment.polarity)

    for i in range(1, len(an_list)):
        if (an_list[i] > 0):
            label.append('positive')
        elif (an_list[i] < 0):
            label.append('negative')

    rows = zip(tweet_list,label)
    for row in rows:
        thewriter.writerow(row)




