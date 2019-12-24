import tweepy
import time
import random

CONSUMER_KEY = 'sWfMoXhHc69uUcBTfH065kasf'
CONSUMER_SECRET = 'gvurP1VAxFcc1Ng3gZU5g7i1gnm4asZzZ4khbP1o8xIXr9mhRo'
ACCESS_KEY = '1209190595329167366-rAyoKToj7Blz9M3GMTmt9kx0AVttBV'
ACCESS_SECRET = 'yiYAt6Smgqbu1IZuGY31GBjImXxqKgCJxskL9tWXu1OqE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


print('She moves with a purpose')
user = api.me()
print (user.screen_name)

LYRICS = open("BlackMidiLyrics.txt", "r")
counter = 0

while True:
    while counter < 300:
        LYRICSS = list(set(LYRICS.read().splitlines()))
        length = len(LYRICSS)
        for i in range(length):
            api.update_status(LYRICSS[i])
            time.sleep(14400)
            counter += 1
        counter = 0
