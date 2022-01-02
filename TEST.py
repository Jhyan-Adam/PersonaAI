import nltk
import numpy as np
import re
from numpy.core.numeric import outer

from tensorflow_text.python.ops.ngrams_op import Reduction
import Vectoriser
from numpy.core.arrayprint import str_format
import tensorflow as tf
import tensorflow_text as tf_text
import nltk

class TESTCode:
    input_data = tf.ragged.constant([
    [['I', 'having', 'a', 'cat'], ['His', 'name', 'is', 'Mat']],
    [['Do', 'you', 'want', 'to', 'come', 'visit'], ["I'm", 'free', 'tomorrow']],
])
    sentence = "transcribing the text was difficult when i was doing it"
    #word_tokenizer = tf_text.WhitespaceTokenizer()
    #tokens = nltk.word_tokenize(sentence)
    #print("\n", tokens)

    #output = tf_text.ngrams(input_data, width=2, axis=-1, reduction_type=Reduction.STRING_JOIN, string_separator="|||")
    print("\n\n\n")
    #print(output)

    #print(input_data.get_shape())
    data = input_data.numpy()

    lemmatizer = nltk.WordNetLemmatizer()
    #print(tf.get_static_value(data[0, 0])) #DEBUGGING
    #print(data[0, 0])
    #tags = Vectoriser.posTag(input_data)
    #w = Vectoriser.posTag([b"Better", b"moving"])
    #print(tags)
    #print(Vectoriser.get_wordnet_pos('having'))
    word = 'barraging'
    lemmas = lemmatizer.lemmatize(word, pos=Vectoriser.get_wordnet_pos(word))
    #lemmas = Vectoriser.lemmatize(data)
    print(lemmas)
    
class TEST():
    obj = TESTCode()
