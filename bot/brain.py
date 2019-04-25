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

    def load_model(self, path='/home/hyperscypion/Desktop/database.csv'):
        self.data_frame = pd.read_csv(path, header=None)
        return self.data_frame
    
    def create_corpus(self):
        pass

    def predict(self, text):
        pass



