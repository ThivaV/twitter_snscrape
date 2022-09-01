import snscrape.modules.twitter as sntwitter
import pandas as pd

hashtag = "rewarded"

for tweet in sntwitter.TwitterHashtagScraper(hashtag).get_items():
    print(vars(tweet))
    break