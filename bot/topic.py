import nltk
import nltk.stem
import pandas as pd
from nltk.corpus import stopwords
from spacy.lang.pl import Polish
from spacy.lang.pl.examples import sentences

parser = Polish()

words = nltk.word_tokenize('ala ma samochody')

stops = set(nltk.corpus.stopwords.words('polish'))

words = [word for word in words if word not in stops]

print(words)

s = nltk.stem.WordNetLemmatizer()

for word in ['samochód', 'samochody', 'samochodowy']:
    print(s.lemmatize(word))


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
        # Napisać funkcję do wczytywania pytań, odpowiedzi i weryfikacji do 3 osobnych kolumn
        # for i in self.data:


from nltk.corpus import wordnet as wn


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


from nltk.stem.wordnet import WordNetLemmatizer


def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


def pre_lda(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in stops]
    return tokens


print(pre_lda('Ala ma kota i ma czerwony samochód'))

topic = Topic()

topic.load_data()

topic.create_corpus()