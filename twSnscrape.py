import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import date


#query = "(from:elonmusk) until:2020-01-01 since:2010-01-01"

#query = "#NDC_EC until:2022-01-01 since:2018-01-01"
#query = input("Ingrese el Hastag a buscae")
query = '#financiamientoclimáticoEC'
tweets = []

limit = 1000

#limit = 20

fromday = '2015-01-01'
endday = date.today()


for tweet in sntwitter.TwitterSearchScraper(query, fromday,  endday).get_items():

    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.likeCount, tweet.user.location, tweet.retweetCount])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Likes', 'Ubicacion', 'Retweets'])
print(df)

# Para guardar el arvhivo
df.to_csv('tweets.csv')

#Transformamos el archivo csv a excel

import os
import glob
import csv
from xlsxwriter.workbook import Workbook

for csvfile in glob.glob(os.path.join('.', '*.csv')):
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()




