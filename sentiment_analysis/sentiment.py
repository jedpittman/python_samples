import pandas as pd
import nltk
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def getDataFrameFromPath(path:str):
    """Load a csv from input path and return a pandas dataframe
    
    """
    return pd.read_csv(path)

def buildWordCloud(inputCSVPath:str) -> object:
    """Take in an input csv and produce an outputPNGPath"""
    df = getDataFrameFromPath(inputCSVPath)

    # Create stopword list:
    local_stopwords = set(STOPWORDS)
    local_stopwords.update(["br", "href"])

    textt = " ".join(review for review in df.Text)
    return WordCloud(stopwords=local_stopwords).generate(textt)

def saveWordcloudAsPNGAndShow(wordcloudInput: object, outputPNGPath: str):
    """Take an input wordcloud and save as PNG and display"""
    plt.imshow(wordcloudInput, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(outputPNGPath)
    plt.show()


def mainRun():
    """Run the logic to take a csv input and produce a sentiment wordcloud"""
    wordcloud = buildWordCloud('test/Reviews.csv')
    saveWordcloudAsPNGAndShow(wordcloud, 'test/output.png')


if __name__ == "__main__":
    mainRun()