import re
from builtins import print

import pandas as pd


class CustomTokenizer:
    def __init__(self, vocab):
        self.vocab = vocab
        self.word_pattern = re.compile(r"\b(" + "|".join(vocab) + r")\b")
        self.trigram_pattern = re.compile(r"\b(\w+)\s+(\w+)\s+(\w+)\b")

    def tokenize_words(self, text):
        return self.word_pattern.findall(text)

    def tokenize_trigrams(self, text):
        return self.trigram_pattern.findall(text)

def remove_duplicates(text):
    words = text.split()
    return ' '.join(sorted(set(words), key=words.index))

def remove_duplicates_list(lst):
    return list(set(lst))

def join_rows(df):
    rows = df.values.tolist()
    return [' '.join(row) for row in rows]

# create sample dataframe
data = pd.read_excel('Preprocessing/corpus_seg_address.xlsx')

vocab = join_rows(data)
vocab = remove_duplicates_list(vocab)
# print the resulting dataframe
print(vocab)
