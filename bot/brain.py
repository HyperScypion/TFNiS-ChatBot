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

    #   @staticmethod
    def load_model(self, path='/home/hyperscypion/Desktop/database.csv'):
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
        return self.corpus

    def fit_LDA(self, corpus, num_topics=10):
        self.lda = LdaModel(corpus, num_topics)

    def predict(self, text, jaccard=False):
        pass
