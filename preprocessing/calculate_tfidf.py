# Calculate the 400 word with highest tfidf in the documents. This because the BERT context windows is 512 tokens which is roughly 400 words

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd

