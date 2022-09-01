import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "GoGotaHome until:2022-11-16 since:2022-01-14"

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    print(vars(tweet))
    break
