import pandas as pd
df = pd.read_csv('Reviews.csv')
# print(df.head())


import nltk
# from nltk import WordCloud

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#nltk.download('stopwords')
#from nltk.corpus import stopwords
# Create stopword list:
local_stopwords = set(STOPWORDS)
local_stopwords.update(["br", "href"])
textt = " ".join(review for review in df.Text)
wordcloud = WordCloud(stopwords=local_stopwords).generate(textt)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloud11.png')
plt.show()