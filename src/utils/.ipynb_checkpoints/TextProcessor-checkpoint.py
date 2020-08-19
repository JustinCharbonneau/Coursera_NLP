from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import pandas as pd
from sklearn.base import BaseEstimator

class TextProcessor(BaseEstimator):
    
    def __init__(self, tokenized:bool=False, join_tokens:bool=True, 
                 lemmatize:bool=True, remove_stop:bool=True,
                 stop_list:list=None, to_lower:bool=True):
        self.tokenized = tokenized
        self.join_tokens = join_tokens
        self.lemmatize = lemmatize
        self.remove_stop = remove_stop
        self.to_lower = to_lower
        self.stop_list = stop_list
    
    def fit():
        pass
    
    def fit_transform(self, df:pd.DataFrame, col:str):
        """
        Preprocess a text column of choice. Transformations that are included are lemmatizing and stopword removal.

        Args
            df: pd.DataFrame, Pandas dataframe with a text column
            col: str, The text column to apply transformations
            tokenized: bool, Specify if the text column has already been tokenized
            join_tokens: bool, Specify if after the transformations, the data should be converted back into a text string
            lemmatize: bool, Specify if lemmatization is needed
            remove_stop: bool, Specify if stopword removal is needed
        Returns
            df: Preprocessed dataframe with the column modified in-place
        """
        if self.to_lower:
            df[col] = df[col].apply(lambda x: x.lower())
            
        if not self.tokenized:
            # Expects a string-like object
            df[col] = df[col].apply(lambda x: [word for word in word_tokenize(x)])
            
        if self.lemmatize: 
            lemmatizer = WordNetLemmatizer()
            df[col] = df[col].apply(lambda x: [lemmatizer.lemmatize(tokenized_word) for tokenized_word in x])

        if self.remove_stop:
            if self.stop_list:
                print('using custom stop list')
                stop_words = self.stop_list
            else:
                print('using wordnet stop list')
                stop_words = set(stopwords.words('english'))
            df[col] = df[col].apply(lambda x: [lemma_word for lemma_word in x if lemma_word not in stop_words])

        if self.join_tokens:
            df[col] = df[col].apply(lambda x: ' '.join(x))
            
        return df
    
    def transform():
        pass
