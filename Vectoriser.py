import numpy as np
import re
from gensim.corpora import Dictionary
from tensorflow.python.ops.gen_array_ops import empty
import tensorflow as tf
import tensorflow_text as tf_text
from tensorflow_text.python.ops.ngrams_op import Reduction


def preprocess(a):
    pass

def lemmatize(m):
    pass

def lemmatize(m):
    pass
    
def tokenize(m):
    word_tokenizer = tf_text.WhitespaceTokenizer()
    return word_tokenizer.tokenize(m)

def bigramTokenize(a):
    #t = re.findall("[\w]+", m)
    #bigramTokens = np.empty(shape=len(t), dtype=np.dtype('U100'))
    #for i in range(len(t)-1):
    #    bigramTokens[i] = t[i] + " " + t[i+1]
    #return bigramTokens
    return tf_text.ngrams(a, width=2, axis=-1, reduction_type=Reduction.STRING_JOIN, string_separator="|||")

def decimalEncode(t):
    newTkn = u""
    for tkn in t:
        for c in tkn:
            newTkn += str(ord(c))
    return newTkn

def tfidfEncode(t):
    encodedTokens = np.empty(shape=len(t), dtype=float)
    #TODO Code
    return encodedTokens
