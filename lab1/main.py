import nltk

# nltk.download('all')
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import snscrape.modules.twitter as sntwitter
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy.linalg as LA
import numpy as np

# Zad1

# a
text = open("article.txt").read()

# b
tokens = nltk.word_tokenize(text)
print(len(tokens))

# c
stopWords = nltk.corpus.stopwords.words("english")
filteredSentence = [w for w in tokens if not w.lower() in stopWords]
print(len(filteredSentence))

# d
stopWords.extend(['.', ',', '-', '(', ')', '``', '\'\'', '\'s'])
filteredSentence = [w for w in tokens if not w.lower() in stopWords]
print(len(filteredSentence))

# e
lemmatized_sentence = []
lem = nltk.stem.wordnet.WordNetLemmatizer()
for w in filteredSentence:
    lemmatized_sentence.append(lem.lemmatize(w, "v"))
print(len(lemmatized_sentence))

# f
fdist = nltk.probability.FreqDist(lemmatized_sentence)
plot = fdist.most_common(10)
x = []
y = []
for word in plot:
    x.append(word[0])
    y.append(word[1])
plt.bar(x, y)
plt.show()

# g

uniqueString = (" ").join(filteredSentence)
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(uniqueString)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# zad2

# a
bad = open("bad.txt").read()
good = open("good.txt").read()
badOnly = open("badOnly.txt").read()
goodOnly = open("goodOnly.txt").read()


def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")
    print("Sentence Overall Rated As", end=" ")

    if sentiment_dict['compound'] >= 0.05:
        print("Positive")
    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")
    else:
        print("Neutral")


# b, c
sentiment_scores(bad)
sentiment_scores(good)
sentiment_scores(badOnly)
sentiment_scores(goodOnly)

# zad3

tweets_list = []
tweets_list2 = []

for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper('Warszawa since:2022-10-01 until:2022-10-20').get_items()):
    if i > 100:
        break
    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tweets_df.to_csv('tweets.csv', index=False)

# GDA
for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(
            'Warszawa near:"Gdańsk" within:10km since:2022-10-01 until:2022-10-20').get_items()):
    if i > 100:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.place])

tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Place'])
tweets_df2.to_csv('outGda.csv', index=False)

# zad4

# a

text2 = open("text2.txt").read()
text3 = open("text3.txt").read()

filteredSentence2 = [w for w in nltk.word_tokenize(text2) if not w.lower() in stopWords]
lemmatized_sentence2 = []
for w in filteredSentence2:
    lemmatized_sentence2.append(lem.lemmatize(w, "v"))
fdist2 = nltk.probability.FreqDist(lemmatized_sentence2)

filteredSentence3 = [w for w in nltk.word_tokenize(text3) if not w.lower() in stopWords]
lemmatized_sentence3 = []
for w in filteredSentence3:
    lemmatized_sentence3.append(lem.lemmatize(w, "v"))
fdist3 = nltk.probability.FreqDist(lemmatized_sentence3)

docs = [text, text2, text3]
lemmatized_docs = []
for w in docs:
    lemmatized_docs.append(lem.lemmatize(w, "v"))

# DTM
coun_vect = CountVectorizer(lowercase='True', stop_words=stopWords)
dtm = coun_vect.fit_transform(lemmatized_docs)
bow = pd.DataFrame(dtm.toarray(), columns=coun_vect.get_feature_names_out())
print(bow)

# TF
coun_vect = CountVectorizer(lowercase='True', stop_words=stopWords)
dtm = coun_vect.fit_transform(lemmatized_docs)
bow = pd.DataFrame(dtm.toarray(), columns=coun_vect.get_feature_names_out())
print(bow)
bow.values[0] = [float(x) / float(len(lemmatized_sentence)) for x in bow.values[0]]
bow.values[1] = bow.values[1] / len(lemmatized_sentence2)
bow.values[2] = bow.values[2] * len(lemmatized_sentence3)
print(bow)

# TFIDF
tfvec = TfidfVectorizer(lowercase='True', stop_words=stopWords)
tdf = tfvec.fit_transform(lemmatized_docs)
bow = pd.DataFrame(tdf.toarray(), columns=tfvec.get_feature_names_out())
print(bow)
