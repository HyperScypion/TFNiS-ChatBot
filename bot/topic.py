import nltk
import nltk.stem
import pandas as pd
from nltk.corpus import stopwords
from spacy.lang.pl import Polish
from spacy.lang.pl.examples import sentences
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer


parser = Polish()
stops = set(nltk.corpus.stopwords.words('polish'))
words = [word for word in words if word not in stops]


s = nltk.stem.WordNetLemmatizer()


class Topic:

    def __init__(self):
        print('init')

    @staticmethod
    def preapare_data():
        with open('/home/hyperscypion/Desktop/database.chatbot', 'r') as file:
            read = file.read()
            read = read.splitlines()
            for text in read:
                text = text.replace(',', '').replace('|', ',').replace('.', '')
                text += '\n'
                with open('/home/hyperscypion/Desktop/database.csv', 'a') as fout:
                    fout.writelines(text)
        file.close

    def load_data(self, data_path='/home/hyperscypion/Desktop/database.csv'):
        self.data = pd.read_csv(data_path)
        return self.data

    def create_corpus(self):
        print(self.data)
        self.ques = []
        self.answ = []
        self.ver = []

def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


def pre_lda(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in stops]
    return tokens


topic = Topic()

topic.load_data()

topic.create_corpus()
