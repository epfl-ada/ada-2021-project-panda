import os

import pandas as pd
import numpy as np
import requests
import re

from glob import glob
from urllib.parse import urlparse
from dateutil.parser import parse


def clean_chunk(chunk):

  """Filter out the rows in chunk which:
  - have first speaker attribution probability less than 0.5 (empirically)
  - have a None speaker or an empty QID
  Delete the unnecessary columns for our analysis
  """


  # Select the highest probability
  chunk['h_probas'] = chunk.apply(lambda p: p['probas'][0][1], axis=1)
  # Select the corresponding speaker
  chunk['h_probas_speaker'] = chunk.apply(lambda p : p['probas'][0][0], axis=1)
  # Select the associated speaker QID
  chunk['qids'] = chunk.apply(lambda p : p['qids'][0] if len(p['qids']) >= 1 else p['qids'], axis=1)
  

# Filter the rows
  chunk = chunk.loc[(chunk['speaker'] != 'None') &
                    (chunk['h_probas'] > '0.5') &
                    (chunk['qids'].astype(str) != '[]')
                    ]

  return chunk.drop(labels=['probas','h_probas_speaker','quoteID', 'phase'], axis=1)

def is_date(string, fuzzy=False):
  """
  Determine whether a given string can be parsed as a date
  If it can be, return True, otherwise return False.
  @Param : - string : string to be parsed
           - fuzzy : boolean allowing fuzzy parsing
  @Return : - boolean : whether string can be parsed as a date or not"""
  try:
    parse(string, fuzzy = fuzzy)
    return True
  except ValueError:
    return False


def tagfree(string):
  """
  Returns whether a given string is url tag free or not
  """

  # If there is an url in the quotation then it might not be a "real" quotation but rather headlines
  if (re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) != None):
    return False
    
  else:
    return True


def html_tagfree(string):
  """Takes a string and return wether this string is html tag free or not"""

  if(re.search('<.+?>', string) != None): 
    return False
  else :
    return True

def clean_quotations(chunk):
  """
  Filters out the incorrect quotations
  """
  # Find all the quotations that are not a date
  date_mask = chunk.apply(lambda p: not is_date(p['quotation']), axis = 1)
  # Find all the quotations that are tag free
  mask = chunk.apply(lambda p: tagfree(p['quotation']), axis = 1)

  chunk = chunk.loc[(date_mask & mask) , :]            

  return chunk


def talks_about(url_list, key_words_list):
  """Check whether some keywords are inside the urls to retrieve the topics of interest
  @Param : - url_list : list of urls (strings)
           - key_words_list : list of key words (string)
  @Return : True if at least on key word was found in in at least on url, False otherwise """

  for url in url_list :
    if any(key in url for key in key_words_list):
      return True
  
  return False


def topic_selection(chunk, keywords):
  """Select the rows which topic is in keywords list:
  @Param : - chunk : pandas DatFrame to filter
           - Keywords : a list of keywords"""

  topic_relevant_index = chunk.urls.apply(lambda p : talks_about(p, keywords))
  
  return chunk.drop(chunk[~topic_relevant_index].index)


def match_and_merge(chunk, gender):
  """Match a speaker and his/her gender, considering only binary genders
  @Param : - chunk : pandas DataFrame
           - gender : binary gender DataFrame
  @Return :  chunk containing speakers and their gender """

  return chunk.merge(gender.loc[gender['id'].isin(list(chunk['qids'].values))], left_on = 'qids', right_on='id')
  
