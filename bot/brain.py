import random
import numpy as np
import pandas as pd
from jaccard import Jaccard
from gensim import corpora, models
from gensim.models import LdaModel
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary


class Brain:
    def __init__(self):
        pass

    def load_model(self, path='/home/hyperscypion/Desktop/database_lda.csv'):
        self.data_frame = pd.read_csv(path, header=None)
        return self.data_frame

    def create_corpus(self, save=True):
        self.text_to_corp = []
        for i in range(len(self.data_frame)):
            self.text_to_corp.append(self.data_frame[0][i].split())

        self.dictionary = corpora.Dictionary(self.text_to_corp)
        if save == True:
            self.dictionary.save('/tmp/deerwester.dict')
        self.corpus = [self.dictionary.doc2bow(text)
                       for text in self.text_to_corp]
        corpora.MmCorpus.serialize('/tmp/deerwester.mm', self.corpus)
        self.id2word = corpora.Dictionary.load('/tmp/deerwester.dict')
        return self.corpus, self.dictionary

    def fit_LDA(self, corpus, num_topics=10):
        self.lda = LdaModel(corpus, num_topics, id2word=self.id2word)
        return self.lda

    def predict(self, text, dictionary, jaccard=False):
        jacc = Jaccard()
        prediction = -1
        list_of_indexes = []
        list_of_topics = []

        if jaccard == True:
            for i in range(len(self.data_frame)):
                if jacc._compute_index(text, str(self.data_frame[0][i])) > prediction:
                    prediction = jacc._compute_index(text, str(self.data_frame[0][i]))

            for i in range(len(self.data_frame)):
                if jacc._compute_index(text, str(self.data_frame[0][i])) == prediction:
                    list_of_indexes.append(i)
            max_random_index = random.randint(0, len(list_of_indexes) - 1)
            return self.data_frame[1][list_of_indexes[max_random_index]]
        else:
            bow = dictionary.doc2bow(text.split())
            for index, score in sorted(self.lda[bow], key=lambda tup: -1 * tup[1]):
                break
            for i in range(len(self.data_frame)):
                if index == self.data_frame[2][i]:
                    list_of_topics.append(self.data_frame[0][i])

            for i in list_of_topics:
                if jacc._compute_index(text, i) > prediction:
                    prediction = jacc._compute_index(text, i)

            max_random_ans = random.randint(0, len(list_of_topics) - 1)
            return list_of_topics[max_random_ans]
