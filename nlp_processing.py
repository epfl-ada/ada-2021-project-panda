import os
import pandas as pd
import numpy as np

import collections
from collections import Counter
import spacy
import nltk
from nltk.stem.porter import *
import gensim
from gensim.models import Phrases
from gensim.models.phrases import Phraser

nlp = spacy.load('en_core_web_sm')
stemmer = PorterStemmer()


def make_bigrams(texts):
  """Texts should be a list of list of words, large enough
  Returns the bigrams contained in the texts"""
  bigram = Phrases(texts, min_count=15)
  bigram_mod = Phraser(bigram)

  # Returns only bigrams
  bigram_words = [bigram_mod[doc] for doc in texts]
  return [[word for word in sentence if '_' in word] for sentence in bigram_words] 

def processing(quote):
    """
    Process a quote
    @Params : quote : a string
    @Return : the processed quotes
    """

    # Convert into a spacy object
    quote_spacy = nlp(quote)

    # Remove punct and stopwords and less than 2 character word (spacy)
    doc = [token for token in quote_spacy if not token.is_punct and not token.is_stop and len(token.text) > 2]
    
    # Lemmatize (spacy)
    doc = [token.lemma_ for token in doc]

    # Stem (NLTK) : need text 
    # Uncomment for stemming instead of lemmatization
    #doc = [stemmer.stem(token.text) for token in doc]
    
    # Casefold
    doc = [token.casefold() for token in doc]

    return doc


def df_processing(df):
  """
    Process an entire dataframe, per gender
    @Params : df : a pandas dataframe
    @Return : a dictionary containing the processed quotes for each gender
    """

  processed_df = {'M':[], 'F':[]}
  
  # Split gender
  for gender in ['M', 'F']:

    # Put in one list all quotations
    quotes = list(df.loc[df['gender'] == gender]['quotation'].values)

    processed_quotes = []

    # Process each quote
    for quote in quotes_spacy :
      processed = processing(quote)
      processed_quotes.append(processed)
    
    # Add bigrams - TODO I don't know if that works
    bigrams = make_bigrams(processed_quotes)
    processed_and_bigrams_quotes = [q + b for q, b in zip(processed_quotes, bigrams)]
    
    processed_df[gender] = processed_and_bigrams_quotes

  return processed_df
