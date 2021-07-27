import numpy as np
import re
from numpy.core.numeric import outer

from tensorflow_text.python.ops.ngrams_op import Reduction
import Vectoriser
from numpy.core.arrayprint import str_format
import tensorflow as tf
import tensorflow_text as tf_text

class TESTCode:
    input_data = tf.ragged.constant([
    [['I', 'have', 'a', 'cat'], ['His', 'name', 'is', 'Mat']],
    [['Do', 'you', 'want', 'to', 'come', 'visit'], ["I'm", 'free', 'tomorrow']],
])
    "transcribing the text was difficult when i was doing it"
    #word_tokenizer = tf_text.WhitespaceTokenizer()
    #tokens = word_tokenizer.tokenize("transcribing the text was difficult when i was doing it")
    #print(tokens)
    output = tf_text.ngrams(input_data, width=2, axis=-1, reduction_type=Reduction.STRING_JOIN, string_separator="|||")
    print("\n\n\n")
    print(output)

class TEST():
    obj = TESTCode()
