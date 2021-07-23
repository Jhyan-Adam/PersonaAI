import numpy as np
import re
from gensim.corpora import Dictionary


def bigramTokenise(m):
    t = re.findall("[\w]+", m)
    bigramTokens = np.empty(shape=len(t)-1, dtype=np.dtype('U100'))
    for i in range(len(t)-1):
        bigramTokens[i] = t[i] + " " + t[i+1]
    return bigramTokens


def decimalEncodeArr(t):
    tknArr = np.empty(shape=(len(t)), dtype=float)
    cntrIdx = 0
    for tkn in t:
        newTkn = u""
        for c in tkn:
            newTkn += str(ord(c))
            tknArr[cntrIdx] = newTkn
            cntrIdx += 1
    return tknArr

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
