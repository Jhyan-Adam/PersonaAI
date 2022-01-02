from nltk import tag
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize.texttiling import VOCABULARY_INTRODUCTION
import numpy as np
import re
from gensim.corpora import Dictionary
from tensorflow.python.ops.gen_array_ops import empty
import tensorflow as tf
import tensorflow_text as tf_text
from tensorflow_text.python.ops.ngrams_op import Reduction, ngrams
import nltk
from pathlib import Path
import os.path


path = Path("C:/Users/jhyan_8hz0dhz/OneDrive/Documents/AI Projects/PersonaAI/DataStorage/")


def preprocess(a):
    pass


def get_wordnet_pos(w):
    tag = nltk.pos_tag([w])[0][1][0].upper()
    tag_dict = {"J": nltk.corpus.wordnet.ADJ,
                "N": nltk.corpus.wordnet.NOUN,
                "V": nltk.corpus.wordnet.VERB,
                "R": nltk.corpus.wordnet.ADV}

    return tag_dict.get(tag, nltk.corpus.wordnet.NOUN)


def lemmatize(a):
    lemmatizer = nltk.WordNetLemmatizer()
    lclTkns = []
    lemmas = []

    for pkt in a:
        lclTkns = []
        for msg in pkt:
            lclTkns.append(lemmatizer.lemmatize(msg.lower(), pos=get_wordnet_pos(msg.lower())))
        lemmas.append(lclTkns)

    return lemmas


def tokenize(a):
    tknList = []

    for pkt in a:
        for msg in pkt:
            tkns = word_tokenize(msg)
            tknList.append(tkns)
    
    return tknList


def bigramTokenize(a):
    #PS: The tokenise does work on receiverPackets but the ouput is too long for the pring()
    #If I use bigrams the order data is implicitly encoded because only one reconstruction of the bigrams will work

    #t = re.findall("[\w]+", m)
    #bigramTokens = np.empty(shape=len(t), dtype=np.dtype('U100'))
    #for i in range(len(t)-1):
    #    bigramTokens[i] = t[i] + " " + t[i+1]
    #return bigramTokens
    return tf_text.ngrams(a, width=2, axis=-1, reduction_type=Reduction.STRING_JOIN, string_separator="|||")


def getIDF(a, b):
    return a.count(b)


def getVocabulary(bS=None, bR=None):
    #This will take in a bigram array and create a 2D array with the bigram and its idf value
    #If I use bigrams the order data is implicitly encoded because only one reconstruction of the bigrams will work
    vocabulary = []

    if (os.path.isfile("C:/Users/jhyan_8hz0dhz/OneDrive/Documents/AI Projects/PersonaAI/DataStorage/DataStorage/vocabulary.npy") and (bS!=None and bR!=None)):

        for pkt in bS:
            for msg in pkt:
                for bgram in msg:
                    if (bgram not in vocabulary):
                        vocabulary.append([tf.get_static_value(bgram), tf.reshape(bS, [-1]).count(bgram)])
        for pkt in bR:
            for msg in pkt:
                for bgram in msg:
                    if (bgram not in vocabulary):
                        vocabulary.append([tf.get_static_value(bgram), ])

        np.save(path/"vocabulary", vocabulary)
    #return vocabulary #DEBUGGING


def tfidfEncode(a):
    encodedTokens = np.empty(shape=len(a), dtype=float)
    #This will encode a single bigram input and output the corresponding tfidf value?
    #If I use bigrams the order data is implicitly encoded because only one reconstruction of the bigrams will work
    bow = tf.sparse.SparseTensor()
    f = 0
    idf = 0
    #TODO Code
    return encodedTokens







def decimalEncode(t):
    #LEGACY
    newTkn = u""
    for tkn in t:
        for c in tkn:
            newTkn += str(ord(c))
    return newTkn

def oldtokenize(a):
    #LEGACY
    word_tokenizer = tf_text.WhitespaceTokenizer()
    return word_tokenizer.tokenize(a)

#    def posTag(a):
#    tags = []
#    single_msg = []
#    msgs = []

#    for pkt in a:
#        for msg in pkt:
#            for tkn in msg:
#                single_msg.append(tf.get_static_value(tkn).decode("utf-8"))
#                #tkn = lemmatize(tf.get_static_value(tkn).decode("utf-8"))
#            msgs.append(single_msg)
    
#    for msg in msgs:
#        tags.append(nltk.pos_tag(msg, tagset=None))

#    return tags
